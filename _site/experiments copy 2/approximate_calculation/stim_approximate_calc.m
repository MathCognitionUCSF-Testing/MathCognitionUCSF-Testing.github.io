function list_final = StimCalcMMR_Memoria
%% Generate stimuli list for Calculation EBS
% Pedro Pinheiro-Chagas - Stanford 2018
% with Amy Daitch and Josef Parvizi

%% Basic parameters
op_min = 1:9;
op_max = 10:90;
all_op = allcomb(op_max,op_min);
nrep_min = 4; % Number of repetitions of min operand
ndeccross = round(nrep_min/2); % of decade cross.


length(op_min)*4*2

for op = 1:2 % first generate additions and then subtractions
    if op == 1
        corr_res = all_op(:,1)+all_op(:,2);
    else
        corr_res = all_op(:,1)-all_op(:,2);
    end
    
    % Check if decade cross
    for i = 1:size(all_op,1)
        tmp_res_str = num2str(corr_res(i));
        tpm_max_str = num2str(all_op(i,1));
        if (str2num(tmp_res_str(1)) == str2num(tpm_max_str(1))) && str2num(tpm_max_str) ~= 10
            dcross(i) = 0;
        else
            dcross(i) = 1;
        end
    end
    list = [all_op corr_res dcross'];
    
    for i = op_min
        % List all decade cross and no decade cross for each min
        pdcross = list(list(:,2)==i & list(:,4)==1,:);
        ndecros = list(list(:,2)==i & list(:,4)==0,:);
        % Randomly select problems
        list_tmp{i} = [pdcross(randsample(1:size(pdcross,1),ndeccross),:);ndecros(randsample(1:size(ndecros,1),nrep_min-ndeccross),:)];
    end
    
    % Final list
    list_tmp = vertcat(list_tmp{:});
    list_tmp(:,end+1) = repmat(op,length(list_tmp),1);
    list_final{op} = list_tmp;
    clear list_tmp
end

% Concatenate additions and subtractions
list_final = vertcat(list_final{:});
for i = 1:length(list_final)
    if list_final(i,end) == 1
        problem{i,1} = [num2str(list_final(i,1)) ' + ' num2str(list_final(i,2))];
        operation(i,1) = 1;
    else
        problem{i,1} = [num2str(list_final(i,1)) ' - ' num2str(list_final(i,2))];
        operation(i,1) = -1;
    end
end
l.problem = problem;
l.max_op = list_final(:,1);
l.operation = operation;
l.min_op = list_final(:,2);
l.result = list_final(:,3);
l.dec_cross = list_final(:,4);

for i = 1:length(list_final)
    %% Add deviants
    if rem(i,2) == 1
        if l.operation(i,1) == 1
            l.pres_result(i,1) = l.result(i) + 2;
        else
            l.pres_result(i,1) = l.result(i) - 2;
                if l.pres_result(i,1) < 0
                    l.pres_result(i,1) = l.result(i) + 2;
                else
                end
        end
        l.correct(i,1) = 0;
    else
        l.pres_result(i,1) = l.result(i);
        l.correct(i,1) = 1;
    end
    
    
    
    %% Operation and decade cross
    if l.operation(i,end) == 1
        op = 'add';
    else
        op = 'sub';
    end
    if l.dec_cross(i,end) == 1
        dc = 'decross';
    else
        dc = 'no_decross';
    end
    l.conds_addsub{i,1} = op;
    l.conds_decross{i,1} = dc;
    l.conds_addsub_decross{i,1} = [op '_' dc];
end
% stimulation scheme
list = struct2table(l);

for i = 1:length(list_final)
        list.problem{i,1} = [list.problem{i} ' = ' num2str(list.pres_result(i))];
end

%% Randomize list
list_final = shuffleTable(list);

end
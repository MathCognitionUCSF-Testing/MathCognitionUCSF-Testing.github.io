function table_in = shuffleTable(table_in)
    %% Shuffle the rows of table
    % Pedro Pinheiro-Chagas - Stanford 2018
    
    rand_order = randperm(size(table_in,1));
    col_names = table_in.Properties.VariableNames;
    for i = 1:length(col_names)
        table_in.(col_names{i}) = table_in.(col_names{i})(rand_order,:);
    end

end
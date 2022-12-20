%% Nonsymbolic stimuli 

num1 = 10:5:30;
num2 = 10:5:30;

allcombs = allcomb(num1,num2);
allcombs = allcombs(allcombs(:,1)./allcombs(:,2)~=1,:);

list = {};

stim_table = table;
for i = 1:size(allcombs,1)
    figure('units', 'normalized', 'outerposition', [0 0 .3 .3]) % [0 0 .6 .3]
    plot(rand(allcombs(i,1),1,1), '.', 'MarkerSize', 30, 'Color', 'blue')
    hold on
    plot(rand(allcombs(i,2),1,1), '.', 'MarkerSize', 30, 'Color', 'red')
    axis square
    axis off
    set(gcf,'color','w');
    set(gca,'color','w');

    filename = ['img/dots', '_', num2str(allcombs(i,1)), '_', num2str(allcombs(i,2)), '.png'];
    if allcombs(i,1) > allcombs(i,2)
       resp = 'f';
    else
       resp = 'j';
    end

    stim_table.correct_response(i) = {resp};
    stim_table.stimulus(i) = {filename};
    stim_table.fixation(i) = {'<div style="font-size:60px;">+</div>'};
    stim_table.fixation_duration(i) = randsample([250:100:1000],1);
%     trial = sprintf('%s%s%s%s%s%s%s%s%s%s', '{ stimulus: ', "'", 'img/', filename, "'", ',  correct_response: ', "'", resp, "'", '},');


    %list = [list; trial];
    f = gcf;
    %exportgraphics(f,filename,'Resolution',100)
    close all
end

str=jsonencode(stim_table, PrettyPrint=true);
str = ['var test_stimuli = ', str];

fid = fopen('stimuli.js', 'w');
fprintf(fid, '%s', str);
fclose(fid)


writematrix(str,'stimuli.json')



writetable(table(list), 'list.csv')










num1 = 10:5:30;
num2 = 10:5:30;

allcombs = allcomb(num1,num2);
allcombs = allcombs(allcombs(:,1)./allcombs(:,2)~=1,:);

p = nsidedpoly(1000, 'Center', [0 0], 'Radius', 2.r);
plot(p, 'FaceAlpha', 0)

list = {};

dot_size_rage = 20:40;

for i = 1:size(allcombs,1)

    figure('units', 'normalized', 'outerposition', [0 0 .5 .5]) % [0 0 .6 .3]
    subplot(1,2,1)  
    v11 = zscore(rand(allcombs(i,1),1,1));
    v12 = zscore(rand(allcombs(i,1),1,1));

    for ii = 1:length(v11)
        hold on
        plot(v11(ii), v12(ii), '.', 'MarkerSize', randsample(dot_size_rage,1), 'Color', 'k')
    end

    hold on
    plot(p, 'FaceAlpha', 0)
    axis square
    axis off
    set(gcf,'color','w');
    set(gca,'color','w');
    subplot(1,2,2)    

    v21 = zscore(rand(allcombs(i,2),1,1));
    v22 = zscore(rand(allcombs(i,2),1,1));

    for ii = 1:length(v21)
        hold on
        plot(v21(ii), v22(ii), '.', 'MarkerSize', randsample(dot_size_rage,1), 'Color', 'k')
    end

    hold on
    plot(p, 'FaceAlpha', 0)
    axis square
    axis off
    set(gcf,'color','w');
    set(gca,'color','w');

    filename = ['dots', '_', num2str(allcombs(i,1)), '_', num2str(allcombs(i,2)), '.png'];
    if allcombs(i,1) > allcombs(i,2)
       resp = 'f';
    else
       resp = 'j';
    end

    trial = sprintf('%s%s%s%s%s%s%s%s%s%s', '{ stimulus: ', "'", 'img/', filename, "'", ',  correct_response: ', "'", resp, "'", '},');


    list = [list; trial];
    f = gcf;
    filename_save = ['/Users/pinheirochagas/Pedro/Stanford/code/MathCognitionUCSF.github.io/experiments/img/', filename];
    exportgraphics(f,filename_save,'Resolution',100)
    close all
end






axis equal

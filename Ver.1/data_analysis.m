clc, clear, close all

data = importdata('database.txt');

samko           = data.data(:,1);
kika            = data.data(:,2);
together        = data.data(:,3);
dates           = data.textdata(2:end,1);
dates_indent    = [{'-'};dates];
graph_length    = length(samko);

subplot 211
hold on
bar([samko,kika,together])
grid minor
grid on
plot([0 10],[1500 1500],'k','LineWidth',3)
legend('Samko','Kika','Spolu','1500 CZK')
axis([0 graph_length+1 0 max(together)])
xticklabels(dates_indent)

subplot 212
plot(together,'k','LineWidth',3)
axis([1 length(together) 1000 max(together)+500])
xticklabels(dates)
grid minor
grid on


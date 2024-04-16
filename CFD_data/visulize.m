% a= readtable('C:\Users\wendell\Documents\Github\CFD_test\CFD_data\test.csv');
% %%
x = [0,1,2];
y = [0,1,2];
%%
data =  csvread('C:\Users\wendell\Documents\Github\CFD_test\CFD_data\test.csv');
%%
i=485
z_485 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=490
z_490 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=495
z_495 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=500
z_500 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=505
z_505 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=510
z_510 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=515
z_515 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=520
z_520 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=525
z_525 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=530
z_530 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=535
z_535 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
i=540
z_540 = [data(i,13) , data(i,30), data(i,3); data(i,29), data(i,23), data(i,28); data(i,18), data(i,31), data(i,8)]
%%
% x = b(1,:)
% y = b(2,:)
% z = b(3,:)
%%
% [X,Y] = meshgrid(x,y)
[X,Y]=meshgrid(min(x):max(x),min(y):max(y));
%%
figure()
hold on
subplot(4,3,1)
title('485')
contourf(X,Y,z_485)
caxis([21 25])

subplot(4,3,2)
title('490')
contourf(X,Y,z_490)
caxis([21 25])

subplot(4,3,3)
title('495')
contourf(X,Y,z_495)
caxis([21 25])

subplot(4,3,4)
title('500')
contourf(X,Y,z_500)
caxis([21 25])

subplot(4,3,5)
title('505')
contourf(X,Y,z_505)
caxis([21 25])

subplot(4,3,6)
title('510')
contourf(X,Y,z_510)
caxis([21 25])

subplot(4,3,7)
title('515')
contourf(X,Y,z_515)
caxis([21 25])

subplot(4,3,8)
title('520')
contourf(X,Y,z_520)
caxis([21 25])

subplot(4,3,9)
title('525')
contourf(X,Y,z_525)
caxis([21 25])

subplot(4,3,10)
title('530')
contourf(X,Y,z_530)
caxis([21 25])

subplot(4,3,11)
title('535')
contourf(X,Y,z_535)
caxis([21 25])

subplot(4,3,12)
title('540')
contourf(X,Y,z_540)
caxis([21 25])





% subplot (7,1,7)
% colorbar()

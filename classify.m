clear
D5file = dir('D5_*.tif');
D6file = dir('D6_*.tif');
edge = 0:3:255;
D5h = cell(length(D5file),20);
D6h = cell(length(D6file),20);
for i = 1:length(D5file)
    info = imfinfo(D5file(i).name);
    num_frames = length(info)/2;
    for j = 1:num_frames
        im = imread(D5file(i).name,j);
        im = imresize(im,[100,100]);
        im = double(im)/65535;
        im = im2uint8(im);
        v = double(im(im>2));
        h = histogram(v,edge);
        h.Normalization = 'probability';
        D5h{i,j} = h.Values;
        weighted_mean = 0;
        for k = 1:length(h.Values)
            weighted_mean = h.Values(k)*k + weighted_mean;
        end
        D5hwm(i,j) = weighted_mean;
    end
end
for i = 1:length(D6file)
    info = imfinfo(D6file(i).name);
    num_frames = length(info)/2;
    for j = 1:num_frames
        im = imread(D6file(i).name,j);
        im = imresize(im,[100,100]);
        im = double(im)/65535;
        im = im2uint8(im);
        v = double(im(im>2));
        h = histogram(v,edge);
        h.Normalization = 'probability';
        D6h{i,j} = h.Values;
        weighted_mean = 0;
        for k = 1:length(h.Values)
            weighted_mean = h.Values(k)*k + weighted_mean;
        end
        D6hwm(i,j) = weighted_mean;
    end
end


#### def convolutionLayer(double[][][] input, double[][][][] filter, double[] bias, int stride, double[][][] output, double[][][] dropOutMask, boolean isTest){
def convolutionLayer(inp,f,b,s,m):
	for (int dim = 0; dim < filter.length; dim++):
		for (int filterNo = 0; filterNo < filter[dim].length; filterNo++):
			for (int row = 0; row < input[filterNo].length; row++):
				for (int col = 0; col < input[filterNo][0].length; col++):
					if (col + filter[dim][filterNo].length > input[filterNo][0].length
							|| row + filter[dim][filterNo].length > input[filterNo].length):
						break;

					double[][] submatrix = submatrix(input[filterNo], row, col, filter[dim][filterNo].length);
					if (dropOut && dropOutMask != null):
						double[][] submatrixMask = submatrix(dropOutMask[filterNo], row, col,
								filter[dim][filterNo].length);
						if (isTest):
							output[dim][row][col] += dropOutRate
									* convolute(submatrix, submatrixMask, filter[dim][filterNo]);
						else:
							output[dim][row][col] += convolute(submatrix, submatrixMask, filter[dim][filterNo]);


				else:
						output[dim][row][col] += convolute(submatrix, filter[dim][filterNo]);




	O_WIDTH=(len(inp)-S_EXT+2*PAD)/s+1
	o=[]
	for i in range(0,len(o),1):
		for j in range(0,len(o[i]),1):
			for k in range(0,len(o[i][j]),1):
				# if (!dropOut || dropOutMask == null):
				#	output[i][j][k]=relu(output[i][j][k]+biasInitialValue*bias[i])
				# else:
				output[i][j][k]=relu(output[i][j][k]+biasInitialValue*bias[i])
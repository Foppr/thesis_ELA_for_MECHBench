import numpy as np

class MultimodalWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Wave component with multiple frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            wave += amp * np.sin(freq * x_scaled[i] * np.pi) * np.cos(freq * x_scaled[i] * np.pi * 0.5)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                center_i = np.sin(i * 0.4) * 0.7
                center_j = np.cos(j * 0.3) * 0.6
                sigma = 0.5 + 0.2 * np.sin(i * 0.2)
                rbf += np.exp(-((x_scaled[i] - center_i)**2 + (x_scaled[j] - center_j)**2) / (2 * sigma**2))
        
        # Polynomial interaction terms with mixed degrees
        poly = 0.0
        for i in range(self.dim):
            poly += x_scaled[i]**4 + 0.5 * x_scaled[i]**3 + 0.3 * x_scaled[i]**2
        
        # Cross-terms creating complex interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) * 0.1
                
        # Saddle point component with hyperbolic tangent transitions
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(x_scaled[i] * 2.0) * np.sin(x_scaled[i] * 3.0)
        
        # Combined function with modified weights
        return 1.2 * wave + 0.8 * rbf + 0.6 * poly + 0.4 * cross + 0.3 * saddle
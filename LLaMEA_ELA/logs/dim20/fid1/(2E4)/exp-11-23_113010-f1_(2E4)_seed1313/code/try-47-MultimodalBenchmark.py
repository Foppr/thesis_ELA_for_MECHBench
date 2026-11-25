import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Layered sinusoidal components with varying frequencies and amplitudes
        layer1 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        layer2 = np.sum(np.sin(10 * np.pi * x_norm**2) * np.cos(5 * np.pi * x_norm**2))
        layer3 = np.sum(np.sin(12 * np.pi * x_norm**3) * np.cos(6 * np.pi * x_norm**3))
        
        # Enhanced polynomial basin terms with mixed degrees and adaptive coefficients
        poly_basin = np.sum(0.7 * x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm)
        
        # Stronger cross-dimensional interaction using Gaussian kernel with variable bandwidth
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += np.exp(-2 * dist**2) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle structure with higher-order terms and adaptive scaling
        saddle = np.sum(x_norm**6 * np.cos(3 * np.pi * x_norm) + 0.5 * x_norm**5 * np.sin(2 * np.pi * x_norm))
        
        # Additional harmonic components for increased complexity
        harmonic = np.sum(np.sin(15 * np.pi * x_norm**4) * np.cos(7 * np.pi * x_norm**4))
        
        # Add noise and scale the function
        noise = 0.01 * np.random.random()
        
        return 2.0 * (layer1 + layer2 + layer3) + 1.0 * poly_basin + 0.8 * cross_interaction + 0.5 * saddle + 0.3 * harmonic + noise
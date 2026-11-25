import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Layered sinusoidal components with varying frequencies and amplitudes
        layer1 = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        layer2 = np.sum(np.sin(13 * np.pi * x_norm**2) * np.cos(7 * np.pi * x_norm**2))
        layer3 = np.sum(np.sin(15 * np.pi * x_norm**3) * np.cos(8 * np.pi * x_norm**3))
        
        # Enhanced polynomial basin terms with mixed degrees and adaptive coefficients
        poly_basin = np.sum(0.8 * x_norm**5 + 0.6 * x_norm**4 + 0.3 * x_norm**3 + 0.15 * x_norm**2 + 0.05 * x_norm)
        
        # Stronger cross-dimensional interaction using Gaussian kernel with variable bandwidth
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += np.exp(-3 * dist**2) * np.sin(4 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle structure with higher-order terms and adaptive scaling
        saddle = np.sum(x_norm**7 * np.cos(4 * np.pi * x_norm) + 0.6 * x_norm**6 * np.sin(3 * np.pi * x_norm))
        
        # Additional harmonic components for increased complexity
        harmonic = np.sum(np.sin(18 * np.pi * x_norm**4) * np.cos(9 * np.pi * x_norm**4))
        
        # Novel hyper-sinusoidal terms with non-integer exponents
        hyper_sin = np.sum(np.sin(20 * np.pi * np.power(np.abs(x_norm), 1.5)) * np.cos(10 * np.pi * np.power(np.abs(x_norm), 1.5)))
        
        # Multi-scale interaction terms with varying coupling strengths
        multi_scale = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                multi_scale += (np.exp(-dist**2) * np.sin(5 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) + 
                               0.3 * np.exp(-2*dist**2) * np.cos(6 * np.pi * (x_norm[i] - x_norm[j])))
        
        # Add noise and scale the function
        noise = 0.02 * np.random.random()
        
        return 2.5 * (layer1 + layer2 + layer3) + 1.2 * poly_basin + 1.0 * cross_interaction + 0.6 * saddle + 0.4 * harmonic + 0.3 * hyper_sin + 0.7 * multi_scale + noise
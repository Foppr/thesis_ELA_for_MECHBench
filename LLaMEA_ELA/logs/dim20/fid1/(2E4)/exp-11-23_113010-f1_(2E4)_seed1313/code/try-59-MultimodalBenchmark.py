import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial basin terms with varying degrees and adaptive coefficients
        poly_basin = np.sum(0.4 * x_norm**7 + 0.3 * x_norm**6 + 0.25 * x_norm**5 + 0.15 * x_norm**4)
        
        # Sinusoidal modulations with multiple frequencies and amplitudes
        sin_mod = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(6 * np.pi * x_norm**2) * np.cos(4 * np.pi * x_norm**2))
        
        # Cross-dimensional coupling with interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Asymmetric saddle structure with higher-order terms
        saddle = np.sum(x_norm**8 * np.cos(5 * np.pi * x_norm) + 0.7 * x_norm**7 * np.sin(4 * np.pi * x_norm))
        
        # Additional harmonic components for increased complexity
        harmonic = np.sum(np.sin(15 * np.pi * x_norm**3) * np.cos(10 * np.pi * x_norm**3))
        
        # Add noise and scale the function
        noise = 0.01 * np.random.random()
        
        return 1.7 * poly_basin + 0.9 * sin_mod + 0.7 * sin_mod2 + 0.8 * cross_interaction + 0.5 * saddle + 0.4 * harmonic + noise
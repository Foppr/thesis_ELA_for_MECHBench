import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial basin terms with varying degrees and adaptive coefficients
        poly_basin = np.sum(0.3 * x_norm**6 + 0.4 * x_norm**5 + 0.2 * x_norm**4 + 0.1 * x_norm**3)
        
        # Sinusoidal modulations with prime frequencies and altered amplitudes
        sin_mod = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(11 * np.pi * x_norm**2) * np.cos(7 * np.pi * x_norm**2))
        
        # Enhanced cross-dimensional coupling with cubic interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with modified higher-order terms
        saddle = np.sum(x_norm**7 * np.cos(5 * np.pi * x_norm) + 0.7 * x_norm**6 * np.sin(4 * np.pi * x_norm))
        
        # Additional harmonic components with increased complexity
        harmonic = np.sum(np.sin(13 * np.pi * x_norm**3) * np.cos(9 * np.pi * x_norm**3))
        
        # Add noise and scale the function
        noise = 0.01 * np.random.random()
        
        return 1.5 * poly_basin + 0.8 * sin_mod + 0.6 * sin_mod2 + 0.7 * cross_interaction + 0.4 * saddle + 0.3 * harmonic + noise
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with modified Fibonacci coefficients and higher-order terms
        poly_basin = np.sum(0.42 * x_norm**8 + 0.22 * x_norm**6 + 0.15 * x_norm**5 + 0.08 * x_norm**4)
        
        # Sinusoidal modulations with altered Fibonacci frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(11 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(16 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(25 * np.pi * x_norm**2) * np.cos(16 * np.pi * x_norm**2) * np.sin(20 * np.pi * x_norm**2))
        
        # Modified cross-dimensional coupling with quintic interaction terms and altered Fibonacci-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**4 + x_norm[j]**4) * np.sin(11 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with modified Fibonacci higher-order terms and asymmetric components
        saddle = np.sum(x_norm**9 * np.cos(10 * np.pi * x_norm) + 0.5 * x_norm**7 * np.sin(9 * np.pi * x_norm) + 0.3 * x_norm**6 * np.cos(6 * np.pi * x_norm))
        
        # Additional harmonic components with modified fractal-like complexity
        harmonic = np.sum(np.sin(35 * np.pi * x_norm**3) * np.cos(28 * np.pi * x_norm**3) * np.sin(36 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.02 * np.random.random()
        
        return 2.3 * poly_basin + 0.9 * sin_mod + 0.7 * sin_mod2 + 0.8 * cross_interaction + 0.5 * saddle + 0.4 * harmonic + noise
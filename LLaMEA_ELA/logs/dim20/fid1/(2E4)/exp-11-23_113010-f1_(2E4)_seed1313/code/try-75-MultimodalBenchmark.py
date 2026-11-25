import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with Fibonacci-based coefficients and higher-order terms
        poly_basin = np.sum(0.3 * x_norm**8 + 0.2 * x_norm**7 + 0.1 * x_norm**6 + 0.05 * x_norm**5)
        
        # Sinusoidal modulations with Fibonacci frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(21 * np.pi * x_norm**2) * np.cos(13 * np.pi * x_norm**2) * np.sin(17 * np.pi * x_norm**2))
        
        # Enhanced cross-dimensional coupling with quintic interaction terms and Fibonacci-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**5 + x_norm[j]**5) * np.sin(8 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with Fibonacci higher-order terms and asymmetric components
        saddle = np.sum(x_norm**9 * np.cos(8 * np.pi * x_norm) + 0.5 * x_norm**8 * np.sin(7 * np.pi * x_norm) + 0.3 * x_norm**7 * np.cos(6 * np.pi * x_norm))
        
        # Additional harmonic components with fractal-like complexity
        harmonic = np.sum(np.sin(29 * np.pi * x_norm**3) * np.cos(23 * np.pi * x_norm**3) * np.sin(31 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.015 * np.random.random()
        
        return 2.0 * poly_basin + 0.8 * sin_mod + 0.6 * sin_mod2 + 0.7 * cross_interaction + 0.4 * saddle + 0.3 * harmonic + noise
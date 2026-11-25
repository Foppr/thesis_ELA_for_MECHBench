import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with modified Fibonacci coefficients and higher-order terms
        poly_basin = np.sum(0.35 * x_norm**9 + 0.18 * x_norm**7 + 0.12 * x_norm**6 + 0.06 * x_norm**5)
        
        # Sinusoidal modulations with altered Fibonacci frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * np.sin(14 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(22 * np.pi * x_norm**2) * np.cos(14 * np.pi * x_norm**2) * np.sin(18 * np.pi * x_norm**2))
        
        # Modified cross-dimensional coupling with quintic interaction terms and altered Fibonacci-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**5 + x_norm[j]**5) * np.sin(9 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with modified Fibonacci higher-order terms and asymmetric components
        saddle = np.sum(x_norm**10 * np.cos(9 * np.pi * x_norm) + 0.45 * x_norm**8 * np.sin(8 * np.pi * x_norm) + 0.25 * x_norm**7 * np.cos(7 * np.pi * x_norm))
        
        # Additional harmonic components with modified fractal-like complexity
        harmonic = np.sum(np.sin(30 * np.pi * x_norm**3) * np.cos(24 * np.pi * x_norm**3) * np.sin(32 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.015 * np.random.random()
        
        return 2.1 * poly_basin + 0.85 * sin_mod + 0.65 * sin_mod2 + 0.75 * cross_interaction + 0.45 * saddle + 0.35 * harmonic + noise
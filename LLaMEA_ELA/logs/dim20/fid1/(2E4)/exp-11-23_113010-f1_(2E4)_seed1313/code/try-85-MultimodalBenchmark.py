import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with modified Fibonacci coefficients and higher-order terms
        poly_basin = np.sum(0.42 * x_norm**11 + 0.22 * x_norm**9 + 0.15 * x_norm**8 + 0.08 * x_norm**7)
        
        # Sinusoidal modulations with altered Fibonacci frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(13 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * np.sin(21 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(34 * np.pi * x_norm**2) * np.cos(21 * np.pi * x_norm**2) * np.sin(27 * np.pi * x_norm**2))
        
        # Modified cross-dimensional coupling with septic interaction terms and altered Fibonacci-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**7 + x_norm[j]**7) * np.sin(13 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with modified Fibonacci higher-order terms and asymmetric components
        saddle = np.sum(x_norm**12 * np.cos(13 * np.pi * x_norm) + 0.5 * x_norm**9 * np.sin(10 * np.pi * x_norm) + 0.3 * x_norm**8 * np.cos(9 * np.pi * x_norm))
        
        # Additional harmonic components with modified fractal-like complexity
        harmonic = np.sum(np.sin(42 * np.pi * x_norm**3) * np.cos(34 * np.pi * x_norm**3) * np.sin(37 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.025 * np.random.random()
        
        return 2.5 * poly_basin + 1.1 * sin_mod + 0.8 * sin_mod2 + 1.0 * cross_interaction + 0.6 * saddle + 0.4 * harmonic + noise
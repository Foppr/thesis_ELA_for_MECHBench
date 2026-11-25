import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with modified Fibonacci coefficients and higher-order terms
        poly_basin = np.sum(0.37 * x_norm**10 + 0.20 * x_norm**8 + 0.14 * x_norm**6 + 0.07 * x_norm**5)
        
        # Sinusoidal modulations with altered Fibonacci frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(15 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(23 * np.pi * x_norm**2) * np.cos(15 * np.pi * x_norm**2) * np.sin(19 * np.pi * x_norm**2))
        
        # Modified cross-dimensional coupling with sextic interaction terms and altered Fibonacci-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**6 + x_norm[j]**6) * np.sin(10 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with modified Fibonacci higher-order terms and asymmetric components
        saddle = np.sum(x_norm**11 * np.cos(10 * np.pi * x_norm) + 0.47 * x_norm**9 * np.sin(9 * np.pi * x_norm) + 0.27 * x_norm**8 * np.cos(8 * np.pi * x_norm))
        
        # Additional harmonic components with modified fractal-like complexity
        harmonic = np.sum(np.sin(31 * np.pi * x_norm**3) * np.cos(25 * np.pi * x_norm**3) * np.sin(33 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.016 * np.random.random()
        
        return 2.2 * poly_basin + 0.87 * sin_mod + 0.67 * sin_mod2 + 0.77 * cross_interaction + 0.47 * saddle + 0.37 * harmonic + noise
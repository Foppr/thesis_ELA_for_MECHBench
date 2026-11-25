import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin terms with adaptive coefficients and higher-order terms
        poly_basin = np.sum(0.4 * x_norm**7 + 0.3 * x_norm**6 + 0.2 * x_norm**5 + 0.1 * x_norm**4)
        
        # Sinusoidal modulations with chaotic frequency ratios and varying amplitudes
        sin_mod = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(13 * np.pi * x_norm**2) * np.cos(9 * np.pi * x_norm**2) * np.sin(11 * np.pi * x_norm**2))
        
        # Enhanced cross-dimensional coupling with quartic interaction terms and prime-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**4 + x_norm[j]**4) * np.sin(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with chaotic higher-order terms and asymmetric components
        saddle = np.sum(x_norm**8 * np.cos(7 * np.pi * x_norm) + 0.6 * x_norm**7 * np.sin(6 * np.pi * x_norm) + 0.4 * x_norm**6 * np.cos(5 * np.pi * x_norm))
        
        # Additional harmonic components with fractal-like complexity
        harmonic = np.sum(np.sin(17 * np.pi * x_norm**3) * np.cos(13 * np.pi * x_norm**3) * np.sin(19 * np.pi * x_norm**3))
        
        # Add chaotic noise and scale the function
        noise = 0.02 * np.random.random()
        
        return 1.8 * poly_basin + 0.9 * sin_mod + 0.7 * sin_mod2 + 0.8 * cross_interaction + 0.5 * saddle + 0.4 * harmonic + noise
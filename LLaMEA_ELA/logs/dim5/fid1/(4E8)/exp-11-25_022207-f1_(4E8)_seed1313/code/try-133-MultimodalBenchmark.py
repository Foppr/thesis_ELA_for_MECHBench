import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = np.sum(np.sin(2 * np.pi * x_norm) * 
                              np.cos(3 * np.pi * x_norm) * 
                              np.sin(5 * np.pi * x_norm))
        
        # Radial basis function with Gaussian kernels
        rbfs = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                rbfs += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(4 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle point with exponential weighting
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 1)**3 * np.exp(-0.5 * x_norm[i]**2) * (1 + 0.3 * np.sin(7 * x_norm[i]))
        
        # Chaotic perturbation using logistic map
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.log(1 + np.abs(x_norm[i])) * np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Non-separable polynomial interaction with cosine modulation
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i] * x_norm[j])**2 * np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Multi-scale harmonic component with varying amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += (np.sin(10 * x_norm[i]) + 0.5 * np.sin(20 * x_norm[i]) + 
                        0.3 * np.sin(30 * x_norm[i])) * np.exp(-0.1 * x_norm[i]**2)
        
        # Asymmetric quartic term with exponential decay
        quartic = 0.0
        for i in range(self.dim):
            quartic += x_norm[i]**4 * (1 + 0.5 * np.sin(3 * x_norm[i])) * np.exp(-0.3 * np.abs(x_norm[i]))
        
        return sin_component + rbfs + saddle + chaotic + poly_interaction + harmonic + quartic
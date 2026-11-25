import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multiple sine frequencies and phase shifts
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(15 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) + 
                       np.sin(8 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]))
        
        # Higher-order polynomial potential with non-convex terms
        poly_potential = np.sum(x_norm**6 + 0.8 * x_norm**5 + 0.4 * x_norm**4 + 0.3 * x_norm**3)
        
        # Complex wave interference with varying amplitudes and frequencies
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += (np.sin(3 * np.pi * x_norm[i] * (i + 1)) * 
                        np.cos(4 * np.pi * x_norm[i] * (i + 1)) * 
                        np.sin(2 * np.pi * x_norm[i] * (i + 2)))
        
        # Stronger cross-dimensional coupling with radial basis interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = abs(x_norm[i] - x_norm[j])
                cross_coupling += np.exp(-distance**2) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Radial basis function component with multiple centers
        radial_basis = 0.0
        for i in range(self.dim):
            radial_basis += np.exp(-5.0 * (x_norm[i] - 0.5)**2) + np.exp(-3.0 * (x_norm[i] + 0.3)**2)
        
        # Asymmetric saddle point with mixed degree terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**3 * np.cos(6 * np.pi * x_norm[i]) + x_norm[i]**2 * np.sin(5 * np.pi * x_norm[i])
        
        # Add deterministic chaos scaling and noise with time-varying amplitude
        noise = 0.05 * np.random.random() * (1.0 + 0.5 * np.sin(10 * np.pi * np.sum(x_norm)))
        
        return 2.0 * chaotic + 0.8 * poly_potential + 0.7 * wave_sum + 0.5 * cross_coupling + 0.4 * radial_basis + 0.3 * saddle + noise
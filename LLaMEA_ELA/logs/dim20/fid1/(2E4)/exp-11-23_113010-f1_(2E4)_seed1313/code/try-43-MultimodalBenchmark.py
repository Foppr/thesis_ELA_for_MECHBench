import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multiple logistic map iterations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(20 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]) + 
                       np.sin(8 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i]))
        
        # Modified polynomial potential with higher-degree terms and altered weights
        poly_potential = np.sum(1.2 * x_norm**5 + 0.8 * x_norm**4 + 0.35 * x_norm**3 + 0.2 * x_norm**2)
        
        # Complex sinusoidal wave interference with multiple frequencies and phases
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += (np.sin(6 * np.pi * x_norm[i] * (i + 1)) * np.cos(8 * np.pi * x_norm[i] * (i + 1)) +
                        np.sin(3 * np.pi * x_norm[i] * (i + 2)) * np.cos(9 * np.pi * x_norm[i] * (i + 2)))
        
        # Stronger cross-dimensional coupling with exponential and trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (np.exp(-4*abs(x_norm[i] - x_norm[j])) * 
                                 np.sin(5*np.pi * (x_norm[i] + x_norm[j])) * 
                                 np.cos(3*np.pi * (x_norm[i] - x_norm[j])))
        
        # Augmented saddle point structure with higher-order quartic and quintic terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**5 * np.cos(3 * np.pi * x_norm[i]) + 
                      0.7 * x_norm[i]**4 * np.sin(2 * np.pi * x_norm[i]))
        
        # Additional chaotic noise with dynamic scaling
        noise = 0.025 * np.random.random()
        
        # Combine all components with adjusted weights for increased complexity
        return 3.0 * chaotic + 0.8 * poly_potential + 1.2 * wave_sum + 0.9 * cross_coupling + 0.7 * saddle + noise
import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial potential component with mixed degrees
        poly_potential = 0.0
        for i in range(self.dim):
            poly_potential += (x_scaled[i]**4 + 0.5 * x_scaled[i]**3 - 0.3 * x_scaled[i]**2 + 0.1 * x_scaled[i])
        
        # Trigonometric coupling terms with frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.cos(x_scaled[i])
                freq_j = 1.0 + 0.5 * np.sin(x_scaled[j])
                trig_coupling += np.sin(freq_i * x_scaled[i] + freq_j * x_scaled[j]) * \
                                np.cos(freq_i * x_scaled[i] - freq_j * x_scaled[j])
        
        # Chaotic saddle point component using a modified Henon map
        chaotic_saddle = 0.0
        for i in range(self.dim):
            x_henon, y_henon = 0.1, 0.1
            for _ in range(20):
                x_new = 1.4 - 0.3 * x_henon**2 + y_henon
                y_new = 0.3 * x_henon
                x_henon, y_henon = x_new, y_new
            chaotic_saddle += np.sin(10.0 * x_henon * x_scaled[i]) * np.cos(8.0 * x_henon * x_scaled[i])
        
        # Fractal-like structure using a recursive cosine composition
        fractal_structure = 0.0
        for i in range(self.dim):
            val = x_scaled[i]
            for _ in range(5):
                val = np.cos(val)
            fractal_structure += val**2
        
        # Cross-dimensional interaction with variable coupling strength
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin(0.5 * (x_scaled[i] + x_scaled[j]))
                cross_interaction += coupling_strength * np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Ridge-like structure with varying heights
        ridge_structure = 0.0
        for i in range(self.dim):
            ridge_structure += np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        
        # Global minimum attraction term
        global_min_attraction = 0.0
        for i in range(self.dim):
            global_min_attraction += (x_scaled[i] - 0.5)**2 + (x_scaled[i] + 0.5)**2
        
        # Final combined function with adjusted weights
        return 1.2 * poly_potential + 0.9 * trig_coupling + 1.5 * chaotic_saddle + \
               0.7 * fractal_structure + 0.8 * cross_interaction + 0.6 * ridge_structure + \
               0.4 * global_min_attraction
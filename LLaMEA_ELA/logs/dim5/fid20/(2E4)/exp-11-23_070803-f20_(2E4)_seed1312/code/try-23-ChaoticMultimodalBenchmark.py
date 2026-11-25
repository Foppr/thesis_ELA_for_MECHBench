import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Enhanced polynomial basin with adaptive powers and coupling
        basin_term = 0
        for i in range(self.dim):
            basin_term += (0.5 * np.abs(x_norm[i])**8 + 
                          0.4 * np.abs(x_norm[i])**5 + 
                          0.3 * np.abs(x_norm[i])**3 + 
                          0.2 * x_norm[i]**2)
        
        # Fractal-like chaotic component with recursive frequency modulation
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = np.sin(25 * np.abs(x_norm[i] - x_norm[j])) + 1.5
                chaotic_term += (np.sin(freq_mod * 20 * x_norm[i] * x_norm[j]) * 
                               np.cos(freq_mod * 15 * (x_norm[i] + x_norm[j])) + 
                               np.cos(freq_mod * 18 * x_norm[i] * x_norm[j]) * 
                               np.sin(freq_mod * 12 * (x_norm[i] - x_norm[j])))
        
        # Multi-scale multimodal component with varying frequency ranges
        multimodal_term = 0
        for i in range(self.dim):
            multimodal_term += (np.sin(50 * x_norm[i]) * np.cos(45 * x_norm[i]) + 
                              np.sin(60 * x_norm[i]**1.5) * np.cos(55 * x_norm[i]**1.5) +
                              np.sin(70 * x_norm[i]**2.5) * np.cos(65 * x_norm[i]**2.5) +
                              np.sin(80 * np.abs(x_norm[i])**3) * np.cos(75 * np.abs(x_norm[i])**3))
        
        # Adaptive coupling with dynamic phase shifts
        coupling_term = 0
        for i in range(self.dim):
            phase_shift = np.sin(15 * x_norm[i])
            coupling_term += (np.sin(20 * x_norm[i]) * np.cos(20 * x_norm[(i+1) % self.dim] + phase_shift) +
                            np.cos(18 * x_norm[i]) * np.sin(18 * x_norm[(i+1) % self.dim] - phase_shift))
        
        # Fractal-like interaction term with self-similar structure
        fractal_term = 0
        for i in range(self.dim):
            fractal_term += (np.sin(35 * x_norm[i]**2) * np.cos(30 * x_norm[i]**2) * 
                           np.sin(25 * x_norm[i]**3) * np.cos(20 * x_norm[i]**3))
        
        # Combine all terms with dynamic weights
        result = 0.8 * basin_term + 1.2 * chaotic_term + 1.5 * multimodal_term + 0.9 * coupling_term + 0.7 * fractal_term
        
        # Add complex non-smooth noise to increase difficulty
        noise = np.random.laplace(0, 0.002, size=1)[0]
        
        return result + noise
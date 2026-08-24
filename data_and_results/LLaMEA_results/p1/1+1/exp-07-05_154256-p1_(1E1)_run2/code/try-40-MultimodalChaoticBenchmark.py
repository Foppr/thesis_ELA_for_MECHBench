import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.5
        self.c2 = 2.0
        self.c3 = 1.5
        self.chaos_factor = 0.3
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_term = self.c1 * r**4 + self.c2 * r**2
        
        # Sinusoidal wave component with multiple frequencies
        wave_term = 0
        for i in range(self.dim):
            wave_term += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Chaotic perturbation using logistic map
        chaotic_term = 0
        logistic_r = 3.8
        for i in range(self.dim):
            if i == 0:
                chaotic_term += logistic_r * x[i] * (1 - x[i]**2)
            else:
                chaotic_term += logistic_r * x[i] * (1 - x[i-1]**2)
                
        # Cross-term interactions with polynomial coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(np.pi * (x[i] + x[j]))
                
        # Additional multimodal component with multiple peaks
        multi_peak = 0
        for i in range(self.dim):
            multi_peak += np.sin(5 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Combine all terms with adaptive weights
        total = radial_term + wave_term + self.chaos_factor * chaotic_term + cross_term + 0.5 * multi_peak
        
        # Add noise-like perturbation for increased complexity
        noise = np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return total + 0.1 * noise
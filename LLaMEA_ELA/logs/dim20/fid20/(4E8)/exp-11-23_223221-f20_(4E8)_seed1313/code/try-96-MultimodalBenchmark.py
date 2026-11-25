import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like oscillatory terms with quaternion-inspired symmetry
        fractal_term = 0.0
        for i in range(self.dim):
            # Use quaternion-based frequency modulation and phase shifts
            freq1 = 2.0 + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            freq2 = 1.8 + 0.6 * np.cos(i * 0.5) * np.sin(i * 0.4)
            # Add chaotic modulation with noise coupling
            noise = np.random.normal(0, 0.05) if i % 3 == 0 else 0
            fractal_term += (0.5 * np.sin(freq1 * x[i] + noise) * 
                            np.cos(freq2 * x[i] + noise) * 
                            np.exp(-0.2 * np.abs(x[i])) + 
                            0.25 * np.sin(4 * freq1 * x[i]) * 
                            np.cos(3 * freq2 * x[i]) +
                            0.15 * np.sin(7 * x[i]) * np.exp(-0.1 * x[i]**2) +
                            0.1 * np.sin(2 * x[i]**3) * np.cos(x[i]))
        
        # Modified adaptive ridge structure with chaotic scaling
        ridge_term = 0.0
        for i in range(self.dim):
            # Apply a chaotic ridge function with multi-scale exponential components
            ridge_height = 0.7 * (1 + np.tanh(x[i] / (0.9 + i * 0.2))) * (1 - np.exp(-0.6 * x[i]**2))
            # Add chaotic modulation
            chaos_mod = 1 + 0.1 * np.sin(5 * x[i])
            ridge_term += ridge_height * np.exp(-0.4 * x[i]**2) * chaos_mod
        
        # Enhanced cross-dimensional interaction with chaotic distance scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended interaction range
                # Use chaotic distance-based scaling with sine-wave modulation
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                scale_factor = 1.0 / (1.0 + dist**4) * np.exp(-0.15 * dist) * np.sin(3 * dist)
                cross_term += scale_factor * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j])
        
        # Improved global modulation with chaotic polynomial and trigonometric components
        global_mod = 0.0
        for i in range(self.dim):
            # Apply chaotic combination of polynomial and sinusoidal scaling
            global_mod += 0.4 * (x[i]**5) * np.exp(-0.12 * np.abs(x[i])) * np.sin(0.7 * x[i]) + \
                         0.2 * x[i]**3 * np.cos(0.9 * x[i]) + \
                         0.1 * np.sin(4 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Add chaotic noise component to increase landscape irregularity
        noise_component = 0.05 * np.sum(np.random.normal(0, 1, self.dim) * x)
        
        return fractal_term + ridge_term + cross_term + global_mod + noise_component + 0.02 * np.sum(x**2)
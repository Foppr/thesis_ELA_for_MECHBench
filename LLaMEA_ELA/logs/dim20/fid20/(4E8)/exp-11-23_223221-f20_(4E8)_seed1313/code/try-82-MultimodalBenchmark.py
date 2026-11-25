import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like oscillatory terms with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Use dimension-dependent base frequency with chaotic modulation
            freq = 2.0 + 0.8 * np.sin(i * 0.5 + 1.0) * np.cos(i * 0.3)
            # Combine multiple sine/cosine waves with varying amplitudes and phases
            fractal_term += (0.4 * np.sin(freq * x[i]) * 
                            np.cos(1.2 * freq * x[i]) * 
                            np.exp(-0.15 * np.abs(x[i])) + 
                            0.2 * np.sin(2.5 * freq * x[i]) * 
                            np.cos(1.8 * freq * x[i]) * 
                            np.exp(-0.05 * x[i]**2))
        
        # Improved adaptive ridge structure with exponential scaling
        ridge_term = 0.0
        for i in range(self.dim):
            # Enhanced ridge with dimension-dependent steepness and width
            ridge_height = 0.6 * (1 + np.tanh(x[i] / (0.8 + i * 0.15)))
            ridge_width = 0.3 + 0.2 * np.sin(i * 0.4)
            ridge_term += ridge_height * np.exp(-ridge_width * x[i]**2)
        
        # Stronger cross-dimensional interaction with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-3), i):  # Bidirectional limited interaction
                # Distance-based scaling with logarithmic behavior
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                scale_factor = 1.0 / (1.0 + dist**1.5)
                cross_term += scale_factor * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Enhanced global modulation with polynomial and trigonometric components
        global_mod = 0.0
        for i in range(self.dim):
            # Combine cubic, quartic, and sinusoidal scaling for complex global structure
            global_mod += 0.3 * (x[i]**4) * np.exp(-0.1 * np.abs(x[i])) * np.sin(0.7 * x[i]) + \
                         0.15 * (x[i]**2) * np.cos(1.5 * x[i])
        
        # Add a small noise component to increase ruggedness
        noise = 0.01 * np.sum(np.sin(x * 10.0))
        
        return fractal_term + ridge_term + cross_term + global_mod + noise
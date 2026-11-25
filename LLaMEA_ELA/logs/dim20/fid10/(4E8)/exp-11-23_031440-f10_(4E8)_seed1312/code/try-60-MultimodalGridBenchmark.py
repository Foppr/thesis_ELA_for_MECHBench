import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin with dynamic scaling
        basin_term = 0.1 * np.sum(x**2) * (1.0 + 0.1 * np.sin(0.5 * np.sum(x**2)))
        
        # Grid of global minima terms with chaotic perturbations and multi-scale patterns
        grid_minima = 0.0
        for i in range(self.dim):
            # Multi-frequency sine-cosine pattern with chaotic modulation
            freq1 = 3 * (1 + 0.2 * np.sin(x[i]))
            freq2 = 4 * (1 + 0.15 * np.cos(x[i] * 0.5))
            grid_minima += np.sin(freq1 * np.pi * x[i] / 2.0) * np.cos(freq2 * np.pi * x[i] / 1.5)
            
        # Enhanced sinusoidal interference terms with dynamic coupling coefficients
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling that varies with position
                coupling = 0.5 * (1 + 0.3 * np.sin(x[i] + x[j]))
                interference += coupling * np.sin(2 * np.pi * (x[i] + x[j])) * np.cos(2 * np.pi * (x[i] - x[j]))
        
        # Complex noise term with chaotic and multi-scale components
        noise = 0.02 * np.sum(np.sin(5 * x) + np.cos(3 * x) + 0.5 * np.sin(7 * x) + 
                             0.1 * np.sin(13 * x) * np.cos(9 * x))
        
        # Enhanced multimodal component with chaotic frequency modulation and exponential decay
        multimodal = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation
            freq_mod = 4 * (1 + 0.25 * np.sin(x[i] * 0.3))
            multimodal += 0.3 * (np.sin(freq_mod * np.pi * x[i]) + 
                               np.cos(2 * freq_mod * np.pi * x[i])) * np.exp(-0.1 * x[i]**2)
            
        # Cross-term interactions with dynamic conditioning and chaotic coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Condition number that varies with position and dimension
                condition = 1.0 + 0.5 * np.sin(x[i] * x[j] * 0.1)
                cross_terms += condition * (x[i]**2 + x[j]**2) * np.sin(0.5 * np.pi * (x[i] - x[j]))
        
        # Add a chaotic conditioning term that varies with the entire solution vector
        chaos_condition = 0.05 * np.sum(np.sin(10 * x) * np.cos(8 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Add a multi-scale harmonic pattern for increased complexity
        multiscale = 0.0
        for k in range(1, 6):
            multiscale += 0.05 * np.sin(k * np.pi * np.sum(x)) * np.cos(k * np.pi * np.sum(x**2))
        
        return basin_term + grid_minima + interference + noise + multimodal + cross_terms + chaos_condition + multiscale
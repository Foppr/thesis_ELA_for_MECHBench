import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term with dynamic scaling and chaotic modulation
        basin_term = 0.1 * np.sum(x**2) * (1.0 + 0.1 * np.sin(0.5 * np.sum(x**2)))
        
        # Grid of global minima terms with enhanced chaotic perturbations and multi-scale patterns
        grid_minima = 0.0
        for i in range(self.dim):
            # Multi-frequency sine-cosine pattern with enhanced chaotic modulation
            freq1 = 3 * (1 + 0.3 * np.sin(x[i] * 0.7))
            freq2 = 4 * (1 + 0.2 * np.cos(x[i] * 0.4))
            grid_minima += np.sin(freq1 * np.pi * x[i] / 2.0) * np.cos(freq2 * np.pi * x[i] / 1.8)
            
        # Enhanced sinusoidal interference terms with dynamic coupling coefficients
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling that varies with position and dimension
                coupling = 0.6 * (1 + 0.4 * np.sin(x[i] + x[j]))
                interference += coupling * np.sin(2 * np.pi * (x[i] + x[j])) * np.cos(2 * np.pi * (x[i] - x[j]))
        
        # Complex noise term with enhanced chaotic and multi-scale components
        noise = 0.03 * np.sum(np.sin(5 * x) + np.cos(3 * x) + 0.6 * np.sin(7 * x) + 
                             0.15 * np.sin(13 * x) * np.cos(9 * x))
        
        # Enhanced multimodal component with improved chaotic frequency modulation and exponential decay
        multimodal = 0.0
        for i in range(self.dim):
            # Improved chaotic frequency modulation
            freq_mod = 5 * (1 + 0.3 * np.sin(x[i] * 0.4))
            multimodal += 0.4 * (np.sin(freq_mod * np.pi * x[i]) + 
                               np.cos(2 * freq_mod * np.pi * x[i])) * np.exp(-0.15 * x[i]**2)
            
        # Cross-term interactions with enhanced dynamic conditioning and chaotic coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced condition number that varies with position and dimension
                condition = 1.0 + 0.6 * np.sin(x[i] * x[j] * 0.15)
                cross_terms += condition * (x[i]**2 + x[j]**2) * np.sin(0.6 * np.pi * (x[i] - x[j]))
        
        # Enhanced chaotic conditioning term that varies with the entire solution vector
        chaos_condition = 0.06 * np.sum(np.sin(10 * x) * np.cos(8 * x) * np.exp(-0.06 * np.sum(x**2)))
        
        # Enhanced multi-scale harmonic pattern for increased complexity
        multiscale = 0.0
        for k in range(1, 7):
            multiscale += 0.06 * np.sin(k * np.pi * np.sum(x)) * np.cos(k * np.pi * np.sum(x**2))
        
        # Additional harmonic term to improve discrimination
        additional_harmonic = 0.02 * np.sum(np.sin(4 * x) * np.cos(6 * x))
        
        return basin_term + grid_minima + interference + noise + multimodal + cross_terms + chaos_condition + multiscale + additional_harmonic
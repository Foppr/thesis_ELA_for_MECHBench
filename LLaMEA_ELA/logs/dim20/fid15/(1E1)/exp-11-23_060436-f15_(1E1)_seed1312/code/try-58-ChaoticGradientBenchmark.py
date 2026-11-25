import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        base = np.sum(x**2) * 0.1
        
        # Time-varying chaotic oscillation with memory effect
        chaotic = 0
        for i in range(self.dim):
            # Memory-dependent chaotic modulation
            mem_term = np.sin(x[i] * (1 + 0.1 * np.sin(x[i-1] if i > 0 else x[0]))) * \
                      np.cos(x[i] * (1 + 0.05 * np.cos(x[i-1] if i > 0 else x[0])))
            # Oscillatory component with dynamic frequency
            freq = 2.0 + 1.5 * np.sin(0.3 * i)
            osc_term = np.sin(freq * x[i]) * np.cos(freq * x[i])
            chaotic += mem_term * osc_term
            
        # Multi-scale fractal interference pattern
        fractal = 0
        scales = [0.5, 1.0, 2.0, 3.0]
        for i in range(self.dim):
            for s in scales:
                fractal += np.sin(s * x[i]) * np.cos(s * x[i]) * \
                          np.exp(-((x[i] - s)**2 / (2 * s**2)))
                
        # Dynamic resonance landscape with cross-dimension coupling
        resonance = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Coupling strength varies with dimension index
                coupling = 0.5 + 0.2 * np.sin(0.1 * (i + j))
                resonance += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Adaptive gradient field with directional dependence
        grad_field = 0
        for i in range(self.dim):
            # Directional gradient modulation
            dir_mod = 1.0 + 0.3 * np.sin(0.5 * x[i])
            grad_field += dir_mod * (np.sin(x[i]**2) + np.cos(x[i]**2))
            
        # Ultra-high frequency chaotic modulation with spatial correlation
        high_freq = 0
        for i in range(self.dim):
            # Spatially correlated high-frequency noise
            corr_factor = 1.0 + 0.2 * np.sin(0.7 * x[i])
            high_freq += np.sin(15.0 * x[i]) * np.cos(20.0 * x[i]) * corr_factor
            
        # Combine all components with optimized weights
        return (base * 0.3 +
                chaotic * 0.4 +
                fractal * 0.2 +
                resonance * 0.05 +
                grad_field * 0.03 +
                high_freq * 0.02)
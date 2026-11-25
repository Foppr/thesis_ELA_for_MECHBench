import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillatory components with phase modulation and amplitude scaling
        quantum_osc = np.sum(np.sin(3.0 * x + np.pi * np.random.rand()) * 
                            np.cos(2.0 * x + np.pi * np.random.rand()) * 
                            np.exp(-0.1 * np.abs(x)))
        
        # Fractional Brownian motion-like long-range correlations with Hurst parameter modulation
        fbm_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                fbm_corr += (distance ** (-0.3 + 0.1 * np.sin(i * 0.5))) * np.cos(0.5 * x[i] * x[j])
        
        # Adaptive sigmoidal fitness shaping with dynamic threshold and steepness
        sigmoid_shaping = np.sum(1.0 / (1.0 + np.exp(-2.0 * (x - 1.5 * np.sin(0.3 * x)))))
        
        # Dynamic conditioning based on dimensionality and spatial correlation
        condition_factor = 1.0 + 0.4 * np.sin(self.dim * 0.1) * np.mean(np.abs(x)) + \
                          0.2 * np.cos(self.dim * 0.15) * np.std(x) + \
                          0.3 * np.sin(self.dim * 0.2) * np.max(np.abs(x))
        
        # Rugged polynomial landscape with alternating signs and multi-scale interactions
        rugged_poly = condition_factor * np.sum(x**6 - 2.0 * x**4 + x**2)
        
        # Coupled hyperbolic sine components with varying coupling strengths
        sinh_coupling = 0.5 * np.sum(np.sinh(1.5 * x[:-2] + 0.8 * x[1:-1] - 0.3 * x[2:]))
        
        # Adaptive noise with time-varying intensity and spectral characteristics
        noise_intensity = 0.05 * (1.0 + 0.2 * np.sin(self.dim * 0.1))
        noise = noise_intensity * np.random.randn() * np.sum(np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Combined function value with enhanced complexity and non-stationarity
        return rugged_poly + quantum_osc + fbm_corr + sigmoid_shaping + sinh_coupling + noise
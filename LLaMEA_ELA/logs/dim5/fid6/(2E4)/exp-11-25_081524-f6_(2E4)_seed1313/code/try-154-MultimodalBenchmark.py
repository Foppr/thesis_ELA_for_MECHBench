import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-inspired oscillatory component with self-similar patterns
        fractal_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(0.5 * i) + 0.3 * np.cos(0.7 * i)
            scale = 1.0 + 0.2 * np.sin(0.3 * i)
            fractal_term += scale * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Dynamic Gaussian peaks with adaptive variances and heights
        gaussian_term = 0.0
        num_peaks = min(7, self.dim)
        for i in range(num_peaks):
            center = -4.0 + 8.0 * np.random.rand()
            height = 1.5 + 0.5 * np.sin(0.4 * i)
            variance = 0.2 + 0.6 * np.cos(0.3 * i) ** 2
            gaussian_term += height * np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Enhanced entropy-based ruggedness with multi-scale correlations
        entropy_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            entropy_term += np.abs(diff) * np.exp(-np.abs(diff)) * (1 + 0.4 * np.sin(3.0 * x[i]))
        
        # Novel information-theoretic coupling with dynamic weights
        info_coupling = 0.0
        for i in range(self.dim-2):
            dist = np.abs(x[i] - x[i+1]) + 1e-8
            weight = 0.5 + 0.5 * np.sin(0.5 * i)
            info_coupling += weight * (x[i] * x[i+2]) / dist * np.cos(0.3 * x[i])
        
        # Multi-frequency sine-wave modulation with varying amplitudes and phases
        modulated_term = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.3 * np.sin(0.7 * i)
            phase = 0.1 * np.cos(0.4 * i) + 0.05 * np.sin(0.6 * i)
            modulated_term += amp * np.sin(x[i] + phase) * np.exp(-0.03 * x[i]**2)
        
        # Adaptive scaling based on solution diversity and complexity
        diversity = np.std(x) / (np.max(x) - np.min(x) + 1e-8) if np.max(x) != np.min(x) else 0.0
        complexity = np.mean(np.abs(x)) / 5.0
        scale_factor = 1.0 + 0.4 * diversity + 0.3 * complexity
        
        return (fractal_term + gaussian_term + entropy_term + info_coupling + modulated_term) * scale_factor
import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with modified frequencies
        quantum_component = 0
        for i in range(self.dim):
            freq = 1.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.1 * np.cos(i * np.pi / (self.dim + 2))
            quantum_component += (x[i]**2) * np.sin(freq * x[i] + phase) * np.exp(-0.15 * abs(x[i]))
            
        # Fractional Brownian motion inspired long-range dependence with altered Hurst
        fbm_component = 0
        hurst = 0.6 + 0.3 * np.sin(self.dim * np.pi / 12)
        for i in range(self.dim):
            correlation = 0
            for j in range(i):
                distance = abs(x[i] - x[j])
                correlation += (distance ** (-hurst)) * np.sin(i * j * np.pi / (self.dim + 4))
            fbm_component += correlation * x[i]**2
            
        # Adaptive penalty landscape with modified thresholds
        penalty_component = 0
        for i in range(self.dim):
            # Modified memory-based threshold adjustment
            memory_factor = 1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 5))
            threshold = 2.5 + 1.5 * np.cos(i * np.pi / (self.dim + 6)) * memory_factor
            
            if abs(x[i]) < threshold:
                penalty_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.15 * np.sin(i * np.pi / (self.dim + 7)))
            else:
                penalty_component += (x[i]**3) * np.exp(-0.08 * abs(x[i])) * (1.0 + 0.2 * np.cos(i * np.pi / (self.dim + 8]))
        
        # Saddle-point interaction with modified couplings
        saddle_term = 0
        delay = max(1, int(self.dim / 5))
        for i in range(self.dim):
            for j in range(max(0, i - delay), min(self.dim, i + delay)):
                if i != j:
                    coupling = 0.2 + 0.3 * np.sin((i + j) * np.pi / (self.dim + 2)) * np.cos((i - j) * np.pi / (self.dim + 3))
                    saddle_term += coupling * (x[i]**2 - x[j]**2) * np.exp(-0.03 * abs(i - j))
        
        # Fractal-like curvature with modified scaling
        fractal_component = 0
        for i in range(self.dim):
            scale = 1.2 + 0.4 * np.sin(i * np.pi / (self.dim + 4))
            fractal_component += (abs(x[i]) ** (1.3 + 0.4 * np.cos(i * np.pi / (self.dim + 5)))) * np.sin(scale * x[i])
            
        # Global normalization and scaling with modified exponent
        norm_factor = 1.8 + 0.4 * np.sin(self.dim * np.pi / 15)
        
        # Combine all components with modified weights
        weight1 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 9)
        weight2 = 0.3 + 0.12 * np.sin(self.dim * np.pi / 10)
        weight3 = 0.22 + 0.08 * np.cos(self.dim * np.pi / 11)
        weight4 = 0.23 + 0.15 * np.sin(self.dim * np.pi / 12)
        
        return weight1 * quantum_component + weight2 * fbm_component + weight3 * penalty_component + weight4 * fractal_component * norm_factor
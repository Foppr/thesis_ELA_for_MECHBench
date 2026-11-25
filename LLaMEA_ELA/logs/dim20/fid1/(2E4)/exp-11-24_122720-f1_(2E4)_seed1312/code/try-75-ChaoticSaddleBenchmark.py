import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with complex phase
        quantum_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.2 * np.cos(i * np.pi / (self.dim + 2))
            quantum_component += (x[i]**2) * np.sin(freq * x[i] + phase) * np.exp(-0.1 * abs(x[i]))
            
        # Fractional Brownian motion inspired long-range dependence
        fbm_component = 0
        hurst = 0.7 + 0.2 * np.sin(self.dim * np.pi / 10)
        for i in range(self.dim):
            correlation = 0
            for j in range(i):
                distance = abs(x[i] - x[j])
                correlation += (distance ** (-hurst)) * np.sin(i * j * np.pi / (self.dim + 3))
            fbm_component += correlation * x[i]**2
            
        # Adaptive penalty landscape with memory of previous evaluations
        penalty_component = 0
        for i in range(self.dim):
            # Memory-based threshold adjustment
            memory_factor = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 4))
            threshold = 3.0 + 1.0 * np.cos(i * np.pi / (self.dim + 5)) * memory_factor
            
            if abs(x[i]) < threshold:
                penalty_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 6)))
            else:
                penalty_component += (x[i]**3) * np.exp(-0.1 * abs(x[i])) * (1.0 + 0.15 * np.cos(i * np.pi / (self.dim + 7)))
        
        # Saddle-point interaction with time-delayed couplings
        saddle_term = 0
        delay = max(1, int(self.dim / 4))
        for i in range(self.dim):
            for j in range(max(0, i - delay), min(self.dim, i + delay)):
                if i != j:
                    coupling = 0.3 + 0.4 * np.sin((i + j) * np.pi / (self.dim + 1)) * np.cos((i - j) * np.pi / (self.dim + 2))
                    saddle_term += coupling * (x[i]**2 - x[j]**2) * np.exp(-0.05 * abs(i - j))
        
        # Fractal-like curvature with recursive scaling
        fractal_component = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            fractal_component += (abs(x[i]) ** (1.5 + 0.3 * np.cos(i * np.pi / (self.dim + 4)))) * np.sin(scale * x[i])
            
        # Global normalization and scaling with dynamic exponent
        norm_factor = 2.0 + 0.5 * np.sin(self.dim * np.pi / 12)
        
        # Combine all components with dynamically adjusted weights
        weight1 = 0.3 + 0.1 * np.cos(self.dim * np.pi / 8)
        weight2 = 0.25 + 0.15 * np.sin(self.dim * np.pi / 9)
        weight3 = 0.2 + 0.1 * np.cos(self.dim * np.pi / 10)
        weight4 = 0.25 + 0.15 * np.sin(self.dim * np.pi / 11)
        
        return weight1 * quantum_component + weight2 * fbm_component + weight3 * penalty_component + weight4 * fractal_component * norm_factor
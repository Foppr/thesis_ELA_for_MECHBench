import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with phase modulation
        quantum_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 2))
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 3))
            quantum_component += (x[i]**2) * np.sin(freq * x[i] + phase)
        
        # Fractional Brownian motion inspired fractal component with Hurst parameter
        fbm_component = 0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / 8)
        for i in range(self.dim):
            # Fractal scaling with Hurst exponent
            scale = (abs(x[i]) + 1e-8)**hurst
            fbm_component += scale * np.cos(i * np.pi / (self.dim + 1) * x[i])
        
        # Adaptive penalty landscape with dynamic constraints
        penalty_component = 0
        for i in range(self.dim):
            # Dynamic threshold based on dimensionality
            threshold = 2.0 + 1.0 * np.sin(i * np.pi / (self.dim + 4))
            if abs(x[i]) > threshold:
                penalty_component += (abs(x[i]) - threshold)**3 * (1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2)))
            else:
                penalty_component += -np.log(1.0 + abs(x[i])) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 5)))
        
        # Memory-dependent saddle-point interaction with time-delayed coupling
        memory_saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-delayed coupling strength with memory effect
                delay = int((i + j) % (self.dim // 2 + 1)) if self.dim > 1 else 1
                coupling = 0.8 + 0.2 * np.sin((i + j + delay) * np.pi / (self.dim + 4))
                # Modified saddle interaction with memory dependency
                memory_saddle += coupling * (x[i]**3 - x[j]**3)
        
        # Global normalization and scaling with dynamic factor
        norm_factor = 1.0 + 0.3 * np.cos(self.dim * np.pi / 10)
        
        # Combine all components with modified weights
        weight1 = 0.25 + 0.1 * np.sin(self.dim * np.pi / 5)
        weight2 = 0.30 + 0.15 * np.cos(self.dim * np.pi / 6)
        weight3 = 0.25 + 0.1 * np.sin(self.dim * np.pi / 7)
        weight4 = 0.20 + 0.1 * np.cos(self.dim * np.pi / 8)
        
        # Introduce large mutation: adding a chaotic perturbation term
        chaotic_perturbation = 0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(x[i] * np.exp(-x[i]**2)) * np.cos(x[i] * np.log(abs(x[i]) + 1e-8)) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 7)))
        
        # Introduce nested sinusoidal modulation to the penalty component
        nested_modulation = 0
        for i in range(self.dim):
            nested_modulation += np.sin(3 * x[i]) * np.cos(2 * x[i]**2) * (1.0 + 0.1 * np.sin(i * np.pi / (self.dim + 6)))
        
        # Add chaotic coupling between all dimensions
        chaotic_coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_coupling += np.sin(x[i] * x[j]) * np.exp(-abs(x[i] - x[j]))
        
        return weight1 * quantum_component + weight2 * fbm_component + weight3 * penalty_component + weight4 * memory_saddle * norm_factor + 0.05 * nested_modulation + 0.1 * chaotic_perturbation + 0.02 * chaotic_coupling
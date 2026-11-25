import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with nested phase modulation
        quantum_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 2))
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 3))
            # Nested modulation for increased complexity
            nested_phase = 0.3 * np.sin(freq * x[i] + phase)
            quantum_component += (x[i]**2) * np.sin(freq * x[i] + phase + nested_phase)
        
        # Fractional Brownian motion inspired fractal component with dynamic Hurst parameter
        fbm_component = 0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / 8)
        for i in range(self.dim):
            # Fractal scaling with Hurst exponent and additional chaos factor
            chaos_factor = 1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 5))
            scale = (abs(x[i]) + 1e-8)**hurst * chaos_factor
            fbm_component += scale * np.cos(i * np.pi / (self.dim + 1) * x[i] + 0.5 * np.sin(i * np.pi / (self.dim + 3)))
        
        # Adaptive penalty landscape with dynamic constraints and nested penalties
        penalty_component = 0
        for i in range(self.dim):
            # Dynamic threshold based on dimensionality and chaos factor
            chaos_threshold = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 4))
            threshold = 2.0 + 1.0 * np.sin(i * np.pi / (self.dim + 4)) * chaos_threshold
            if abs(x[i]) > threshold:
                penalty_component += (abs(x[i]) - threshold)**3 * (1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2)))
            else:
                # Nested logarithmic penalty with additional chaotic modulation
                log_term = -np.log(1.0 + abs(x[i])) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 5)))
                chaos_mod = 1.0 + 0.1 * np.cos(i * np.pi / (self.dim + 6))
                penalty_component += log_term * chaos_mod
        
        # Memory-dependent saddle-point interaction with enhanced time-delayed coupling and nested weights
        memory_saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced time-delayed coupling strength with dynamic weights
                delay = int((i + j) % (self.dim // 2 + 1)) if self.dim > 1 else 1
                # Nested weight modulation for increased complexity
                coupling = 0.8 + 0.2 * np.sin((i + j + delay) * np.pi / (self.dim + 4))
                coupling_weight = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 5)) * np.sin(j * np.pi / (self.dim + 6))
                # Modified saddle interaction with memory dependency and chaos factor
                memory_saddle += coupling * coupling_weight * (x[i]**3 - x[j]**3)
        
        # Global normalization and scaling with dynamic factor and nested chaos
        norm_factor = 1.0 + 0.3 * np.cos(self.dim * np.pi / 10)
        chaos_norm = 1.0 + 0.1 * np.sin(self.dim * np.pi / 12)
        
        # Combine all components with modified weights and nested chaos
        weight1 = 0.25 + 0.1 * np.sin(self.dim * np.pi / 5) + 0.05 * np.cos(self.dim * np.pi / 9)
        weight2 = 0.30 + 0.15 * np.cos(self.dim * np.pi / 6) + 0.08 * np.sin(self.dim * np.pi / 11)
        weight3 = 0.25 + 0.1 * np.sin(self.dim * np.pi / 7) + 0.06 * np.cos(self.dim * np.pi / 13)
        weight4 = 0.20 + 0.1 * np.cos(self.dim * np.pi / 8) + 0.07 * np.sin(self.dim * np.pi / 14)
        
        return (weight1 * quantum_component + 
                weight2 * fbm_component + 
                weight3 * penalty_component + 
                weight4 * memory_saddle * norm_factor * chaos_norm)
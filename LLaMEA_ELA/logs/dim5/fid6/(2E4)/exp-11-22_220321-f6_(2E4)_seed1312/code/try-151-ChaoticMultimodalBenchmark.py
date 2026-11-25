import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_order = 8
        self.fractal_dimension = 1.7
        self.ridge_strength = 2.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with quantum-like interference
        poly_term = 0.0
        weights = np.linspace(0.3, 1.8, self.polynomial_order)
        for i in range(self.dim):
            coord = x[i]
            for n in range(1, self.polynomial_order + 1):
                # Quantum phase interference term
                quantum_phase = np.sin(coord * n * 2.0) * np.cos(coord * n * 0.5)
                poly_term += (coord ** n) / (n * (n + 1)) * weights[n-1] * quantum_phase
        
        # Nested fractal Brownian motion with quantum tunneling effects
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.fractal_dimension
            # Multi-scale fractal scaling with quantum tunneling
            scale = (np.abs(coord) ** hurst + 0.1 * np.sin(coord * 3.0)) * (1.0 + 0.2 * np.sin(coord * 7.0))
            fbm_term += scale * np.cos(coord * 1.5) * np.exp(-0.1 * coord**2)
        
        # Dynamic hyper-ridge interactions with quantum superposition
        ridge_term = 0.0
        for i in range(self.dim):
            # Quantum superposition modulation
            mod_val = (np.sin(i * 0.7 + 1.0) * np.cos(x[i] * 0.3) + 
                      0.5 * np.sin(i * 1.3 + 2.0) * np.cos(x[i] * 0.7))
            ridge_mod = 1.0 + self.ridge_strength * (np.sin(x[i] * mod_val) + 
                                                   0.5 * np.cos(x[i] * 2.0) + 
                                                   0.3 * np.sin(x[i] * 3.0))
            ridge_term += ridge_mod * (x[i] ** 2) * np.exp(-0.05 * x[i]**2) * np.cos(x[i] * 0.5)
        
        # Nested cross-dimensional coupling with quantum entanglement
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum entangled interaction term
                asym_interaction = (np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) + 
                                  0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] * x[j]))
                distance = np.abs(x[i] - x[j])
                # Quantum tunneling effect
                cross_term += asym_interaction / (1.0 + distance ** 1.8) * np.exp(-0.2 * distance)
        
        # Multi-frequency global scaling with quantum harmonic modulation
        sum_x = np.sum(x)
        global_scale = (1.0 + 0.3 * np.sin(sum_x * 0.3) * 
                       np.cos(self.dim * 0.2) * 
                       np.exp(-0.1 * sum_x**2) * 
                       (1.0 + 0.1 * np.sin(sum_x * 5.0)))
        
        # Balanced weighted combination with quantum amplitude
        return global_scale * (0.2 * poly_term + 0.25 * fbm_term + 0.25 * ridge_term + 0.3 * cross_term)
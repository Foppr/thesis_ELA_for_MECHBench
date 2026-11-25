import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute stochastic coefficients for polynomial chaos expansion
        self.coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with stochastic coefficients
        chaos_component = 0
        for i in range(self.dim):
            for j in range(5):
                chaos_component += self.coeffs[i, j] * np.polyval([1, 0, -1], x[i]) ** j
        
        # Stochastic harmonic potential with varying amplitudes and frequencies
        harmonic_component = 0
        for i in range(self.dim):
            amp = 1.5 + np.sin(0.5 * i) * 2.0
            freq = 0.8 + np.cos(0.3 * i) * 1.5
            phase = np.random.uniform(0, 2*np.pi) + 0.5 * np.sin(i)
            harmonic_component += amp * np.sin(freq * x[i] + phase) ** 2
        
        # Cross-dimensional coupling with exponential decay and modified interaction
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling_component += np.exp(-dist / (1.5 + 0.2 * i)) * np.sin(3.0 * dist) * np.cos(0.5 * dist)
        
        # Multi-scale oscillation with dynamic scaling factors
        scale_component = 0
        for i in range(self.dim):
            scale_factor = 0.8 + 0.7 * np.sin(0.9 * i)
            scale_component += scale_factor * np.sin(2.5 * x[i]) * np.cos(1.5 * x[i])
        
        # Dimensionality-dependent conditioning with increased variability
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.7)
        
        # Combine all components with modified weights
        return (1.2 * chaos_component + 
                1.8 * harmonic_component + 
                1.0 * coupling_component + 
                1.5 * scale_component + 
                25.0 * condition_factor)
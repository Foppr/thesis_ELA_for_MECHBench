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
            amp = 2.0 + np.sin(0.5 * i) * 1.5
            freq = 1.0 + np.cos(0.3 * i) * 2.0
            phase = np.random.uniform(0, 2*np.pi)
            harmonic_component += amp * np.sin(freq * x[i] + phase) ** 2
        
        # Cross-dimensional coupling with exponential decay
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling_component += np.exp(-dist / (1.0 + 0.1 * i)) * np.sin(2.0 * dist)
        
        # Multi-scale oscillation with dynamic scaling factors
        scale_component = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.7 * i)
            scale_component += scale_factor * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Dimensionality-dependent conditioning
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim)
        
        # Combine all components with dynamic weights
        return (1.5 * chaos_component + 
                2.0 * harmonic_component + 
                0.8 * coupling_component + 
                1.2 * scale_component + 
                20.0 * condition_factor)
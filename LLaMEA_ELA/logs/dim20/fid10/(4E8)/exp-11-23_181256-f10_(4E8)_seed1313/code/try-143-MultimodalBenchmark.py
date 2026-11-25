import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Adaptive radial terms with varying exponents
        radial_term = np.sum((x_scaled**2 + 0.1) * np.exp(-0.5 * x_scaled**2))
        
        # Trigonometric couplings with adaptive frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(3 * (x_scaled[i] + x_scaled[j])) * \
                                np.cos(2 * (x_scaled[i] - x_scaled[j]))
        
        # Exponential interactions with dimension-dependent decay
        exp_interaction = 0.0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.1 * (x_scaled[i]**2)) * \
                             np.sin(5 * x_scaled[i]) * \
                             np.cos(3 * x_scaled[i])
        
        # Multi-scale harmonic components with varying amplitudes
        harmonic_components = 0.0
        for k in range(1, 4):
            harmonic_components += np.sum(np.sin(k * x_scaled) * np.cos(k**2 * x_scaled))
        
        # Adaptive conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components with weighted contributions
        return condition_factor * (1.5 * radial_term + 0.8 * trig_coupling + 
                                  1.2 * exp_interaction + 0.6 * harmonic_components)
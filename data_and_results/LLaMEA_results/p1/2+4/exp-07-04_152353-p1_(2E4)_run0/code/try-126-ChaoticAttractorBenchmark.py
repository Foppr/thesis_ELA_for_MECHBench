import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multimodal component with sinusoidal interference
        modal = 0
        for i in range(self.dim):
            # Sinusoidal interference pattern with varying frequencies
            freq = 2.0 + 0.5 * np.sin(i * 0.5)
            modal += np.sin(x_normalized[i] * freq) * np.cos(x_normalized[i] * freq * 1.5)
        
        # Radial basin component with asymmetric scaling
        radial = 0
        for i in range(self.dim):
            # Asymmetric radial basin with different exponents per dimension
            exponent = 2.0 + 0.3 * np.cos(i * 0.4)
            radial += (x_normalized[i]**2)**(exponent / 2.0)
            
        # Asymmetric gradient field with directional bias
        gradient = 0
        for i in range(self.dim):
            # Directional bias with different weights per dimension
            bias = 1.0 + 0.2 * np.sin(i * 0.3)
            gradient += np.abs(x_normalized[i]) * bias
            
        # Interference pattern with varying amplitudes
        interference = 0
        for i in range(self.dim):
            # Amplitude modulation with exponential decay
            amp = 0.5 + 0.3 * np.exp(-i * 0.1)
            interference += amp * np.sin(x_normalized[i] * 7.0 + i * 0.2)
            
        # Combine all components with modified weights
        result = 0.3 * f1 + 0.25 * modal + 0.2 * radial + 0.15 * gradient + 0.1 * interference
        
        # Add a global perturbation term
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 3))
        result += perturbation
        
        return result
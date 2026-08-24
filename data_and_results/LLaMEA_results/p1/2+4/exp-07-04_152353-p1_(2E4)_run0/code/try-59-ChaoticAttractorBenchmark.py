import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multi-fractal chaotic component with time-delayed feedback
        chaotic = 0
        for i in range(self.dim):
            # Logistic map with time-delayed feedback
            param = 3.95 + 0.05 * np.sin(i * 0.7)
            delayed = x_normalized[i-1] if i > 0 else x_normalized[-1]
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param + 0.1 * delayed)
        
        # Multi-modal nested attractor regions with varying dimensions
        attractor = 0
        for i in range(self.dim):
            # Create multiple nested regions with different attraction points
            region1 = np.abs(x_normalized[i] - np.sin(i * 0.3)) + np.abs(x_normalized[i] + np.cos(i * 0.4))
            region2 = np.abs(x_normalized[i] - np.sin(i * 0.8)) + np.abs(x_normalized[i] + np.cos(i * 0.6))
            region3 = np.abs(x_normalized[i] - np.sin(i * 1.2)) + np.abs(x_normalized[i] + np.cos(i * 0.9))
            attractor += (region1**2.7 + region2**2.3 + region3**2.1)
            
        # Non-smooth component with fractional exponents and multi-scale discontinuities
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents
            exponent = 1.3 + 0.4 * np.sin(i * 0.5)
            smoothness += np.abs(x_normalized[i])**exponent
            
        # Discontinuous gradient regions with multiple discontinuity types
        discontinuous = 0
        for i in range(self.dim):
            # Create multiple types of discontinuities
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                           np.abs(np.sin(x_normalized[i] * 10)) + \
                           np.abs(np.tanh(x_normalized[i] * 2) - x_normalized[i])
            
        # Fractal interference component with wavelet-like interactions
        fractal = 0
        for i in range(self.dim):
            # Wavelet-like interference pattern
            wavelet = np.sin(x_normalized[i] * 15) * np.cos(x_normalized[i] * 8)
            fractal += np.abs(wavelet) * (1 + 0.5 * np.sin(i * 0.3))
            
        # Time-varying multi-objective component
        time_varying = 0
        for i in range(self.dim):
            # Add time-varying weights based on position
            time_weight = 0.5 + 0.5 * np.cos(i * 0.2 + np.sum(x_normalized[:i]) if i > 0 else 0)
            time_varying += time_weight * np.abs(x_normalized[i] - np.sin(i * 0.1))**1.8
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.2 * chaotic + 0.15 * attractor + 0.15 * smoothness + \
                0.1 * discontinuous + 0.1 * fractal + 0.05 * time_varying
        
        # Add high-frequency perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 9) * np.sin(x_normalized * 7))
        result += perturbation
        
        return result
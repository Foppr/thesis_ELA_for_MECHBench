import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with time-dependent frequencies
        chaotic_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i] + 0.1 * self.dim) * np.cos(0.2 * x[i])
            chaotic_component += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic Gaussian mixture with quaternion-inspired weights
        gaussian_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                weight = np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                width = 0.5 + 0.5 * np.sin(0.4 * x[i] + 0.2 * x[j])
                gaussian_component += weight * np.exp(-0.5 * (dist / width)**2)
        
        # Quaternion-inspired coupling with non-commutative interaction
        quat_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-commutative interaction: x[i]*x[j] vs x[j]*x[i]
                term1 = x[i] * np.tanh(x[j]) * np.exp(-0.3 * (x[i] - x[j])**2)
                term2 = x[j] * np.tanh(x[i]) * np.exp(-0.3 * (x[i] - x[j])**2)
                quat_component += (term1 + term2) * np.sin(0.5 * x[i] * x[j])
        
        # Fractal-based dimension scaling with chaotic modulation
        fractal_component = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            fractal_component += scale_factor * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Sharp valley component with hyperbolic tangent modulation
        valley_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                valley_component += np.tanh(10.0 * diff) * np.exp(-0.5 * diff**2)
        
        # Cross-dimensional exponential coupling with chaotic phase shift
        exp_component = 0
        for i in range(self.dim):
            phase = 0.1 * self.dim + 0.05 * np.sin(0.7 * x[i])
            exp_component += np.exp(-0.2 * x[i]**2) * np.cos(phase * x[i])
        
        # Global scaling with chaotic dimension modulation
        scale_factor = 1.5 + 0.5 * np.sin(0.4 * self.dim) * np.cos(0.3 * self.dim)
        
        # Combine all components with varying weights and chaos modulation
        return scale_factor * (0.2 * chaotic_component + 
                              0.25 * gaussian_component + 
                              0.2 * quat_component + 
                              0.15 * fractal_component + 
                              0.1 * valley_component + 
                              0.1 * exp_component)
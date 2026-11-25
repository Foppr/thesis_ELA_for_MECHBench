import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic global basin with variable conditioning
        quadratic = np.sum(x_normalized**2) * (1.0 + 0.5 * np.sin(self.dim * 0.5))
        
        # Enhanced chaotic sinusoidal components with dynamic frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 2) * (1.0 + 0.2 * np.cos(i * 0.7))
            amp = 0.5 + 0.5 * np.sin(i * 0.9) * np.cos(i * 0.3)
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Multi-scale radial basis function components with dynamic centers and widths
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.8) * np.cos(i * 0.4)
            width = 0.1 + 0.3 * np.sin(i * 0.6) * np.cos(i * 0.2)
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * (1.0 + 0.1 * np.sin(i * 0.5))
        
        # Complex cross-dimensional interaction terms with variable coupling strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(6 * (x_normalized[i] + x_normalized[j])) * np.cos(3 * (x_normalized[i] - x_normalized[j]))
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2) * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Non-separable polynomial interaction with higher degree terms and variable exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_factor = 2 + int((i + j) % 4)
                poly_interaction += (x_normalized[i] * x_normalized[j])**exp_factor
        
        # Multi-layer noise using chaotic maps with different parameters and coupling
        noise = 0.0
        r1, r2 = 3.95, 3.85
        x_prev1, x_prev2 = 0.5, 0.3
        for i in range(self.dim):
            x_prev1 = r1 * x_prev1 * (1 - x_prev1)
            x_prev2 = r2 * x_prev2 * (1 - x_prev2)
            noise += np.sin(x_prev1 * 15 * np.pi * x_normalized[i]) * np.cos(x_prev2 * 10 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Additional high-order coupling between all dimensions with trigonometric functions
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    additional_coupling += np.sin(5 * (x_normalized[i] - x_normalized[j])) * np.cos(2 * (x_normalized[i] + x_normalized[j])) * (x_normalized[i]**4 + x_normalized[j]**4)
        
        # Add a complex multi-modal component with multiple peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(8 * x_normalized[i]) * np.cos(4 * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
        
        # Combine all components with carefully tuned weights and dynamic scaling factors
        return (0.3 * quadratic + 
                0.3 * chaotic + 
                0.2 * radial + 
                0.1 * cross + 
                0.05 * poly_interaction + 
                0.05 * noise + 
                0.03 * additional_coupling + 
                0.02 * multimodal)
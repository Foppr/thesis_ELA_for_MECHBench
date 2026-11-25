import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function component with varying widths and centers
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.7) * 0.5
            width = 0.3 + 0.2 * np.cos(i * 0.4)
            rbf += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Sinusoidal oscillations with frequency modulation and amplitude variation
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i * 0.3))
            amp = 1.0 / (1.0 + 0.2 * i)
            sinusoidal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Asymmetric cross-terms with different interaction strengths
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling based on indices
                asymmetry = (i + 1) / (j + 1)
                coupling = 0.5 * (asymmetry + 1.0 / asymmetry)
                term = np.sin(coupling * x_scaled[i] * x_scaled[j]) * np.cos(coupling * x_scaled[i] * x_scaled[j])
                cross_terms += term * (i + j + 1) * 0.1
        
        # Polynomial with mixed even and odd powers for complex curvature
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += 0.3 * x_scaled[i]**2 + 0.2 * x_scaled[i]**3 + 0.1 * x_scaled[i]**4
        
        # Distance-based conditioning with logarithmic scaling
        dist = np.sqrt(np.sum(x_scaled**2))
        conditioning = 0.5 * (self.dim - 1) * np.log(1.0 + dist**2)
        
        # Phase-shifted cubic interactions for enhanced non-separability
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.3 * (i - j))
                cubic_interaction += (x_scaled[i]**3) * (x_scaled[j]**2) * np.cos(phase)
        
        # Combine all components with carefully tuned weights
        return 2.0 * rbf + 1.8 * sinusoidal + 1.5 * cross_terms + 0.8 * polynomial + conditioning + 0.7 * cubic_interaction
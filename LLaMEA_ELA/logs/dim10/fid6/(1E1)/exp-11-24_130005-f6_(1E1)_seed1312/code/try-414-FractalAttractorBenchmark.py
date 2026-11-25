import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with increased complexity and chaotic behavior
        fractal = 0.0
        for i in range(self.dim):
            # Enhanced fractal pattern with higher frequency, amplitude modulation, and chaos
            freq = 4.0 + 1.2 * np.sin(x_scaled[i] * 5.0)
            amp = 2.0 + 0.8 * np.cos(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8) * \
                      np.exp(-0.5 * np.abs(x_scaled[i]))
        
        # Dynamic attractor fields with position-dependent strength and increased chaos
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with varying strengths, positions, and chaotic interactions
            center1 = np.sin(i * 0.7) * 0.9 + 0.1 * np.random.random()
            center2 = np.cos(i * 0.5) * 0.7 + 0.1 * np.random.random()
            center3 = np.sin(i * 0.9) * 0.5 + 0.1 * np.random.random()
            strength1 = 1.5 + 0.4 * np.sin(i * 1.0)
            strength2 = 1.2 + 0.3 * np.cos(i * 0.6)
            strength3 = 0.9 + 0.2 * np.sin(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 2.0) + strength2 * np.exp(-dist2 * 1.5) + strength3 * np.exp(-dist3 * 1.8)
        
        # Dimensionally adaptive complexity with increased interaction range and chaotic terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased interaction range
                # Adaptive interaction based on dimensionality - increased weight and chaos
                weight = 3.0 / (1.0 + np.abs(i - j)**1.5)  # Increased weight and nonlinearity
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.sin(0.7 * (x_scaled[i] + x_scaled[j])**2) * \
                             np.exp(-0.3 * np.abs(i - j))
        
        # Multi-scale fractal component with self-similar structure, increased chaos and complexity
        multiscale = 0.0
        for scale in [1, 2, 3, 4, 6, 8]:  # Added more scales and changed values
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.9) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             np.sin(0.4 * scale * x_scaled[i]) * \
                             np.cos(0.3 * scale * x_scaled[i])
        
        # Sharp transition regions with enhanced sigmoidal boundary effects and chaotic elements
        sharpness = 0.0
        for i in range(self.dim):
            # Sigmoidal transition near critical points - increased sharpness and chaos
            sig1 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] - 0.35)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-40.0 * (x_scaled[i] + 0.35)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-35.0 * (x_scaled[i])))  # Additional transition
            # Add chaotic component to sharp transitions
            chaos = 0.1 * np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i])
            sharpness += (sig1 - 0.5)**2 + (sig2 - 0.5)**2 + (sig3 - 0.5)**2 + chaos**2
        
        # Additional chaotic and nonlinear terms to increase landscape difficulty
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x_scaled[i] * 10.0) * np.cos(x_scaled[i] * 8.0) * \
                           np.exp(-0.2 * x_scaled[i]**2) + \
                           0.5 * np.sin(3.0 * x_scaled[i]) * np.cos(4.0 * x_scaled[i])
        
        # Combined function with modified weighted components for better algorithm discrimination
        return 0.9 * fractal + 1.8 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.7 * sharpness + 0.5 * chaotic_term
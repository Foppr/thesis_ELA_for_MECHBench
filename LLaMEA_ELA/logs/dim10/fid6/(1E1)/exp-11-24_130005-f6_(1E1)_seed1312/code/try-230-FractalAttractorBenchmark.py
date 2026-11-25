import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic sine-cosine patterns and nested frequencies
        fractal = 0.0
        for i in range(self.dim):
            freq1 = 3.0 + 1.5 * np.sin(x_scaled[i] * 4.0)
            freq2 = 2.0 + 0.8 * np.cos(x_scaled[i] * 3.0)
            amp1 = 1.2 + 0.4 * np.sin(x_scaled[i] * 2.0)
            amp2 = 0.9 + 0.3 * np.cos(x_scaled[i] * 1.5)
            fractal += amp1 * np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i] * 0.7) + \
                      amp2 * np.cos(freq1 * x_scaled[i] * 0.5) * np.sin(freq2 * x_scaled[i])
        
        # Enhanced attractor fields with chaotic center positions and dynamic strengths
        attractor = 0.0
        for i in range(self.dim):
            center1 = np.sin(i * 0.8 + 1.0) * 0.9
            center2 = np.cos(i * 0.6 + 0.5) * 0.7
            center3 = np.sin(i * 0.4 + 1.5) * 0.8
            strength1 = 1.5 + 0.5 * np.sin(i * 0.9)
            strength2 = 1.2 + 0.4 * np.cos(i * 0.7)
            strength3 = 0.9 + 0.3 * np.sin(i * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            dist3 = (x_scaled[i] - center3)**2
            
            attractor += strength1 * np.exp(-dist1 * 2.0) + \
                        strength2 * np.exp(-dist2 * 1.5) + \
                        strength3 * np.exp(-dist3 * 3.0)
        
        # High-dimensional complexity with chaotic interaction terms and recursive coupling
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 2.0 / (1.0 + np.abs(i - j) * 0.5)
                # Chaotic coupling with nested sine-cosine interactions
                coupling = np.sin(x_scaled[i] + x_scaled[j]) * \
                          np.cos(x_scaled[i] - x_scaled[j]) * \
                          np.sin(x_scaled[i] * x_scaled[j])
                complexity += weight * coupling
        
        # Multi-scale fractal component with exponentially increasing frequencies and chaotic amplitudes
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Increased scales and added 6
            for i in range(self.dim):
                amp = 1.0 + 0.5 * np.sin(scale * x_scaled[i])
                multiscale += amp * np.sin(scale * x_scaled[i]) * \
                             np.cos(scale * x_scaled[i] * 0.8) * \
                             np.exp(-scale * np.abs(x_scaled[i]) * 0.5)
        
        # Chaotic sharp transition regions with multiple sigmoidal boundaries
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sharp transitions with different steepnesses and positions
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - 0.4)))  # Increased steepness
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + 0.4)))  # Increased steepness
            sig3 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] - 0.2)))  # Even steeper
            sig4 = 1.0 / (1.0 + np.exp(-25.0 * (x_scaled[i] + 0.2)))  # Even steeper
            
            sharpness += (sig1 - 0.5)**3 + (sig2 - 0.5)**3 + \
                        (sig3 - 0.5)**2 + (sig4 - 0.5)**2
        
        # Additional chaotic interference term with nested trigonometric chaos
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nested chaotic interaction with exponentially decaying influence
                influence = np.exp(-0.1 * (i + j))
                interference += influence * np.sin(x_scaled[i] * x_scaled[j] * 5.0) * \
                               np.cos(x_scaled[i] + x_scaled[j] * 2.0)
        
        # Combined function with enhanced weighted components
        return 1.2 * fractal + 1.8 * attractor + 0.8 * complexity + 0.7 * multiscale + 0.6 * sharpness + 0.5 * interference
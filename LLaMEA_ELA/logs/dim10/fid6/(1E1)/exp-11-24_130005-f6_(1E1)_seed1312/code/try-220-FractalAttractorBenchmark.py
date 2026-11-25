import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base fractal component with chaotic recursion and higher order terms
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic fractal pattern with exponential growth in frequency
            freq = 3.0 * np.exp(0.3 * np.abs(x_scaled[i]))
            amp = 1.5 + 0.5 * np.sin(x_scaled[i] * 4.0)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3) * \
                      np.exp(-0.5 * x_scaled[i]**2)
        
        # Multi-attractor field with chaotic positioning and time-dependent strengths
        attractor = 0.0
        for i in range(self.dim):
            # Chaotic attractor centers with dynamic positioning
            center1 = np.sin(i * 0.8 + np.cos(x_scaled[i] * 2.0)) * 0.9
            center2 = np.cos(i * 0.6 + np.sin(x_scaled[i] * 1.5)) * 0.7
            strength1 = 1.2 + 0.3 * np.cos(i * 0.9 + x_scaled[i])
            strength2 = 0.9 + 0.2 * np.sin(i * 0.5 - x_scaled[i])
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7)
        
        # High-dimensional complexity with exponential interaction terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Exponential weight based on dimensionality and distance
                weight = np.exp(-0.1 * (i + j)) * (1.0 + 0.5 * np.sin(i * j * 0.3))
                complexity += weight * np.sin(x_scaled[i] + x_scaled[j]) * \
                             np.cos(x_scaled[i] - x_scaled[j]) * \
                             np.exp(-0.3 * np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale fractal with chaotic frequency modulation and phase shifts
        multiscale = 0.0
        for scale in [1, 2, 3, 6]:  # Increased scale values and added 6
            for i in range(self.dim):
                # Chaotic phase modulation
                phase_mod = np.sin(scale * x_scaled[i] * 0.5) * np.cos(scale * x_scaled[i] * 0.2)
                multiscale += np.sin(scale * x_scaled[i] + phase_mod) * \
                             np.cos(scale * x_scaled[i] * 0.8 + phase_mod) * \
                             np.exp(-scale * np.abs(x_scaled[i]) * 0.5)
        
        # Hyper-sharp transition regions with fractal boundary effects
        sharpness = 0.0
        for i in range(self.dim):
            # Fractal sigmoidal transitions with multiple critical points
            critical_points = [-0.4, -0.2, 0.0, 0.2, 0.4]
            for cp in critical_points:
                sig = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - cp)))  # Increased steepness
                sharpness += (sig - 0.5)**3
        
        # Additional chaotic complexity term with dimensionally scaled parameters
        chaos_term = 0.0
        for i in range(self.dim):
            # Dimensional chaos with exponentially increasing influence
            chaos_factor = np.exp(0.2 * i)
            chaos_term += chaos_factor * np.sin(x_scaled[i] * np.pi * (i + 1)) * \
                         np.cos(x_scaled[i] * np.pi * (i + 2)) * \
                         np.tanh(x_scaled[i])
        
        # Combined function with enhanced weighted components and chaotic scaling
        return 0.8 * fractal + 1.5 * attractor + 0.7 * complexity + 0.6 * multiscale + 0.5 * sharpness + 0.3 * chaos_term
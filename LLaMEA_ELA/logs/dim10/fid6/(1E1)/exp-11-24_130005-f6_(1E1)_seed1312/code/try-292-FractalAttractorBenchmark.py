import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal component with chaotic modulation
        fractal = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation using golden ratio and fibonacci sequence
            freq = 2.0 + 1.5 * np.sin(x_scaled[i] * 3.0 + i * 0.618) * np.cos(x_scaled[i] * 0.5)
            amp = 1.0 + 0.5 * np.sin(x_scaled[i] * 2.0 + i * 1.618) * np.cos(x_scaled[i] * 1.3)
            fractal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5) * \
                      np.exp(-0.1 * np.abs(x_scaled[i]))
        
        # Complex attractor fields with cross-dimensional interactions
        attractor = 0.0
        for i in range(self.dim):
            # Multiple attractor centers with time-varying positions and strengths
            center1 = np.sin(i * 0.5 + np.sum(x_scaled[:min(i+1, self.dim)]) * 0.3) * 0.8
            center2 = np.cos(i * 0.3 + np.sum(x_scaled[:min(i+1, self.dim)]) * 0.2) * 0.6
            strength1 = 1.5 + 0.4 * np.sin(i * 0.7 + np.sum(x_scaled[:min(i+1, self.dim)]) * 0.4)
            strength2 = 1.0 + 0.3 * np.cos(i * 0.4 + np.sum(x_scaled[:min(i+1, self.dim)]) * 0.5)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor += strength1 * np.exp(-dist1) + strength2 * np.exp(-dist2)
        
        # Enhanced complexity with non-linear coupling terms
        complexity = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                # Non-linear interaction with cubic coupling and dimension-dependent weights
                weight = 2.0 / (1.0 + np.abs(i - j)**1.5)  # Increased non-linearity
                coupling = np.sin(x_scaled[i] + x_scaled[j]) * \
                          np.cos(x_scaled[i] - x_scaled[j]) * \
                          np.sin(x_scaled[i] * x_scaled[j])
                complexity += weight * coupling
        
        # Multi-scale fractal with chaotic frequency spectrum and enhanced self-similarity
        multiscale = 0.0
        scales = [1, 2, 3, 5, 7]  # Added more prime scales for chaos
        for scale in scales:
            for i in range(self.dim):
                # Chaotic multi-scale component with varying phase relationships
                phase_shift = np.sin(i * 0.2 + scale * 0.1) * 0.5
                multiscale += np.sin(scale * x_scaled[i] + phase_shift) * \
                             np.cos(scale * x_scaled[i] * 0.7 + phase_shift) * \
                             np.exp(-scale * np.abs(x_scaled[i])) * \
                             (1.0 + 0.2 * np.sin(scale * x_scaled[i]))
        
        # Hyper-chaotic transition regions with multiple sigmoidal boundaries
        sharpness = 0.0
        for i in range(self.dim):
            # Multiple sharp transitions with varying steepness and positions
            transitions = [
                (15.0, 0.3),
                (20.0, -0.3),
                (12.0, 0.0),
                (18.0, 0.6)
            ]
            for steepness, position in transitions:
                sig = 1.0 / (1.0 + np.exp(-steepness * (x_scaled[i] - position)))
                sharpness += (sig - 0.5)**2
        
        # Novel chaotic component with feedback loops and memory effects
        chaotic_component = 0.0
        for i in range(self.dim):
            # Feedback-based chaotic dynamics
            feedback = np.sin(x_scaled[i]) * np.cos(x_scaled[i] * 0.3) * \
                      np.exp(-np.abs(x_scaled[i]))
            chaotic_component += feedback * np.sin(np.sum(x_scaled[:i+1]) * 0.5)
        
        # Combined function with enhanced weighted components and new interaction terms
        return 1.2 * fractal + 1.8 * attractor + 0.7 * complexity + 0.6 * multiscale + \
               0.5 * sharpness + 0.3 * chaotic_component
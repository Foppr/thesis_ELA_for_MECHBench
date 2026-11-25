import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with dynamic scaling
        quadratic = np.sum(x_scaled**2) * (1.0 + 0.1 * np.sin(10.0 * np.sum(x_scaled**2)))
        
        # Chaotic component with nested sinusoidal modulations
        chaotic = 0.0
        for i in range(self.dim):
            # Nested sinusoidal patterns with varying frequencies and amplitudes
            freq1 = 5.0 + 3.0 * np.sin(x_scaled[i] * 2.0)
            freq2 = 8.0 + 4.0 * np.cos(x_scaled[i] * 1.5)
            amp1 = 1.0 + 0.5 * np.sin(7.0 * x_scaled[i])
            amp2 = 0.8 + 0.3 * np.cos(9.0 * x_scaled[i])
            
            # Chaotic modulation using logistic map-like behavior
            chaotic_term = amp1 * np.sin(freq1 * x_scaled[i]) + amp2 * np.cos(freq2 * x_scaled[i])
            chaotic += chaotic_term * np.exp(-0.5 * x_scaled[i]**2)
        
        # Dynamic scaling factors based on position
        dynamic_scale = 1.0
        for i in range(self.dim):
            dynamic_scale *= (1.0 + 0.3 * np.sin(15.0 * x_scaled[i]))
        
        # Adaptive penalty mechanism for deceptive optima
        penalty = 0.0
        for i in range(self.dim):
            # Create deceptive valleys and peaks
            penalty += 2.0 * np.exp(-((x_scaled[i] - 0.3)**2 + (x_scaled[i] + 0.4)**2) / 0.1)
            penalty += 1.5 * np.exp(-((x_scaled[i] + 0.6)**2 + (x_scaled[i] - 0.2)**2) / 0.08)
        
        # Cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with dynamic phase
                phase = np.sin(3.0 * (x_scaled[i] + x_scaled[j]))
                coupling = np.sin(12.0 * np.sqrt((x_scaled[i]**2 + x_scaled[j]**2)) + phase)
                cross_coupling += coupling * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combine all components with adaptive weights
        result = quadratic * dynamic_scale + 1.2 * chaotic + 0.8 * penalty + 0.6 * cross_coupling
        
        # Add adaptive noise based on fitness landscape
        noise_amp = 0.05 * (1.0 + 0.2 * np.sin(25.0 * np.sum(x_scaled**2)))
        noise = noise_amp * np.random.uniform(-1.0, 1.0)
        
        return result + noise
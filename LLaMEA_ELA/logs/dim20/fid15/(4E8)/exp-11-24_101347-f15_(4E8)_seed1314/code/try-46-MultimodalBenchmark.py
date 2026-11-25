import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Periodic force field with chaotic modulation
        force_field = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on position
            freq = 2.5 + 1.2 * np.sin(3.5 * x_scaled[i])
            force_field += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Chaotic gradient modulation with multi-scale interactions
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with chaotic factor
                dist = np.abs(x_scaled[i] - x_scaled[j])
                coupling = np.sin(4.5 * dist) * np.cos(6.5 * dist)
                gradient_mod += coupling * (1.0 + 0.25 * np.sin(11.0 * dist))
        
        # Multi-modal component with dynamic amplitude
        modal_component = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.4 * np.sin(3.5 * x_scaled[i])
            modal_component += amp * np.sin(2.5 * x_scaled[i]) * np.cos(2.5 * x_scaled[i])
        
        # Adaptive conditioning based on distance from origin with exponential scaling
        r = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 1.5 * np.exp(-r**2 / 1.5)
        
        # Combine all terms with dynamic weights
        result = condition_factor * (quadratic + 0.35 * force_field + 0.45 * gradient_mod + 0.55 * modal_component)
        
        # Add small chaotic noise for increased complexity
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result
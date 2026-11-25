import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic periodic force field
        force_field = 0.0
        for i in range(self.dim):
            # Higher frequency chaotic modulation
            freq = 3.0 + 2.0 * np.sin(5.0 * x_scaled[i]) + 0.5 * np.cos(7.0 * x_scaled[i])
            force_field += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Multi-scale cross-dimensional coupling with chaotic interactions
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex distance-based coupling with multiple chaotic factors
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.1)
                coupling = np.sin(8.0 * dist) * np.cos(6.0 * dist) * np.exp(-dist**2)
                gradient_mod += coupling * (1.0 + 0.4 * np.sin(15.0 * dist) * np.cos(13.0 * dist))
        
        # Enhanced multi-modal component with dynamic amplitude and phase
        modal_component = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.8 * np.sin(5.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i])
            phase = 2.0 * np.sin(4.0 * x_scaled[i]) + 0.5 * np.cos(6.0 * x_scaled[i])
            modal_component += amp * np.sin(4.0 * x_scaled[i] + phase) * np.cos(3.0 * x_scaled[i] + phase)
        
        # Advanced radial conditioning with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 3.0 * np.exp(-r**2 / 3.0) + 0.5 * np.sin(10.0 * r)
        
        # Additional high-order trigonometric coupling
        high_order_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j]
                high_order_coupling += np.sin(2.0 * diff) * np.cos(3.0 * diff) * np.tan(1.5 * diff)
        
        # Combine all terms with dynamic weights
        result = condition_factor * (quadratic + 0.4 * force_field + 0.5 * gradient_mod + 0.6 * modal_component + 0.2 * high_order_coupling)
        
        # Add small chaotic noise for increased complexity
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result
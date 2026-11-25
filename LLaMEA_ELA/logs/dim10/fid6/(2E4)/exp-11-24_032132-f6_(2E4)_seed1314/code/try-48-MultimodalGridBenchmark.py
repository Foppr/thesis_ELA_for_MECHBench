import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with exponential density increase
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i != 0 or j != 0:
                    self.global_minima.append([i * 1.2, j * 1.2])
        
        # Add center point as global minimum
        self.global_minima.append([0.0, 0.0])
        self.global_minima = np.array(self.global_minima)
    
    def f(self, x):
        # Handle dimension mismatch by clipping or padding
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]  # Trim to required dimension
        
        # For 2D case (most common for benchmarking)
        if self.dim == 2:
            # Chaotic basin term with exponential growth
            basin_term = 0.5 * np.exp(0.1 * (x[0]**2 + x[1]**2)) - 0.5
            
            # Multimodal terms with varying amplitudes and chaotic distribution
            multimodal_term = 0.0
            for i, center in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - center[0])**2 + (x[1] - center[1])**2)
                amplitude = 1.0 + 0.5 * np.sin(i) + 0.3 * np.cos(i * 2)
                multimodal_term += amplitude * np.exp(-dist**2 / (0.3 + 0.1 * i))
            
            # Add chaotic noise component
            chaotic_noise = 0.2 * np.sin(x[0] * x[1]) * np.cos(x[0] + x[1])
            
            # Return deterministic result without noise
            return basin_term + multimodal_term + chaotic_noise
        
        else:
            # For higher dimensions, use a similar principle but with increased complexity
            # Chaotic basin in first two dimensions
            basin_term = 0.5 * np.exp(0.1 * (x[0]**2 + x[1]**2)) - 0.5
            
            # Multimodal term with chaotic distribution based on dimension
            multimodal_term = 0.0
            key_points = [[i, j] for i in range(-3, 4) for j in range(-3, 4)]
            
            for i, point in enumerate(key_points):
                dist = np.sqrt(sum((x[i % self.dim] - point[i % 2])**2 for i in range(self.dim)))
                amplitude = 1.0 + 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
                multimodal_term += amplitude * np.exp(-dist**2 / (0.4 + 0.05 * i))
            
            # Add dimensionally adaptive chaotic component
            chaotic_component = 0.1 * np.sin(np.sum(x) * 3) * np.cos(np.prod(x) * 0.5)
            
            return basin_term + multimodal_term + chaotic_component
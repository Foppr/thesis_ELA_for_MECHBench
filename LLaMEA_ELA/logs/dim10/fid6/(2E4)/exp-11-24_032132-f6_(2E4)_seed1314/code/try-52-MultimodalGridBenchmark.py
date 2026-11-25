import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with more structured spacing
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i != 0 or j != 0:  # Exclude the center point which is also a minimum
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
            # Enhanced quadratic basin term with directional bias
            basin_term = 0.1 * (x[0]**2 + x[1]**2) + 0.05 * np.sin(x[0]) * np.cos(x[1])
            
            # Multimodal terms - sum of Gaussian peaks at global minima with varying amplitudes
            multimodal_term = 0.0
            for i, center in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - center[0])**2 + (x[1] - center[1])**2)
                # Varying amplitude based on index to create more distinct peaks
                amp = 0.5 * (1 + 0.2 * np.sin(i))
                multimodal_term += amp * np.exp(-dist**2 / 0.4)
            
            # Return deterministic result without noise
            return basin_term + multimodal_term
        
        else:
            # For higher dimensions, use a similar principle but with reduced complexity and added oscillation
            # Enhanced quadratic basin in first two dimensions with oscillatory component
            basin_term = 0.1 * (x[0]**2 + x[1]**2) + 0.03 * np.sin(x[0]) * np.cos(x[1])
            
            # Multimodal term based on distance to key points with dimension-aware scaling
            multimodal_term = 0.0
            key_points = [[i, j] for i in range(-2, 3) for j in range(-2, 3)]
            
            for i, point in enumerate(key_points):
                dist = np.sqrt(sum((x[i] - point[i%2])**2 for i in range(self.dim)))
                # Add dimensionality scaling factor
                scale_factor = 1.0 + 0.1 * (self.dim - 2)
                amp = 0.5 * scale_factor * (1 + 0.1 * np.sin(i))
                multimodal_term += amp * np.exp(-dist**2 / (0.4 * scale_factor))
            
            return basin_term + multimodal_term
import numpy as np

class NestedSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested saddle point structure with hierarchical curvature
        saddle_term = 0.0
        for i in range(self.dim):
            # Hierarchical saddle positions
            saddle_pos = 2.0 * np.sin(0.5 * i) + 0.5 * np.cos(0.3 * i)
            # Adaptive curvature based on dimension
            curvature = 1.0 + 0.3 * np.sin(0.2 * i)
            saddle_term += (x[i] - saddle_pos)**2 * curvature
            
        # Dynamic curvature adaptation with time-varying parameters
        curvature_adapt = 0.0
        for i in range(self.dim):
            # Time-varying adaptation factor
            adapt_factor = 1.0 + 0.5 * np.sin(0.1 * i + 2.0)
            # Curvature modulation based on position
            mod_curvature = 0.5 + 0.5 * np.cos(x[i] * 0.3)
            curvature_adapt += adapt_factor * mod_curvature * x[i]**4
            
        # Spectral noise interference with frequency-dependent attenuation
        noise_term = 0.0
        for i in range(self.dim):
            # Frequency modulation
            freq = 1.0 + 0.8 * np.sin(0.2 * i)
            # Amplitude modulation
            amp = 0.5 + 0.3 * np.cos(0.1 * i)
            # Spectral noise component
            noise_term += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional coupling with nested interaction patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nested interaction strength
                strength = 0.3 + 0.2 * np.sin(0.1 * (i + j))
                # Distance-based coupling with exponential decay
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_term += strength * np.exp(-dist**2) * np.cos(0.5 * (x[i] + x[j]))
                
        # Nested harmonic structure with varying amplitudes and frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            # Nested amplitude modulation
            amp = 1.0 + 0.4 * np.sin(0.3 * i)
            # Nested frequency modulation
            freq = 2.0 + 0.6 * np.cos(0.2 * i)
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Asymmetric basin boundaries with dynamic thresholds
        basin_term = 0.0
        for i in range(self.dim):
            # Dynamic threshold based on dimension
            threshold = 1.5 + 0.5 * np.sin(0.4 * i)
            # Asymmetric penalty function
            if x[i] > threshold:
                basin_term += 0.5 * (x[i] - threshold)**2
            else:
                basin_term += 0.3 * (x[i] - threshold)**2
                
        # Combined function with normalization and scaling
        total = (saddle_term + curvature_adapt + noise_term + cross_term + 
                harmonic_term + basin_term)
        
        return total
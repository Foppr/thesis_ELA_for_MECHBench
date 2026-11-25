import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case based on golden ratio spiral
        if dim == 2:
            angles = np.linspace(0, 2*np.pi*3, 9)  # 9 points in 3 spirals
            radii = np.linspace(0.5, 4.0, 9)
            for i, (angle, radius) in enumerate(zip(angles, radii)):
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                self.global_minima.append([x, y])
        else:
            # For higher dimensions, create a fractal-like structure using recursive pattern
            self.global_minima = [[0.0] * dim]
    
    def f(self, x):
        if len(x) != self.dim:
            # If dimension doesn't match, adjust x to fit
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with varying conditioning
        basin_term = 0.1 * np.sum(x**2)
        
        # Chaotic fractal multimodal term using recursive sine-cosine pattern
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use golden ratio spiral structure with chaotic modulation
            for i, min_pos in enumerate(self.global_minima):
                dx = x[0] - min_pos[0]
                dy = x[1] - min_pos[1]
                dist_sq = dx**2 + dy**2
                
                # Add chaotic modulation based on angle and iteration
                angle = np.arctan2(dy, dx)
                mod_freq = 2.0 + 0.5 * np.sin(i * 0.7)
                chaos_mod = 1.0 + 0.3 * np.sin(angle * mod_freq + i * 0.4)
                
                # Use fractal-like decay with chaotic scaling
                scale_factor = 0.8 + 0.2 * np.cos(i * 0.3)
                height = 0.6 + 0.4 * np.sin(i * 0.5)
                
                multimodal_term += height * chaos_mod * np.exp(-dist_sq / (scale_factor * 0.5))
        else:
            # For higher dimensions, use recursive fractal interaction terms
            # Each pair of dimensions interacts with chaotic scaling and phase shifts
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dx = x[i] - 2.0
                    dy = x[i+1] - 2.0
                    dist_sq = dx**2 + dy**2
                    
                    # Fractal scaling with dimension-dependent phase
                    phase_shift = np.sin(i * 0.3) * np.cos(i * 0.4)
                    scale_factor = 0.5 + 0.3 * np.sin(phase_shift)
                    
                    # Add chaotic modulation based on position
                    chaos_mod = 1.0 + 0.2 * np.sin(x[i] * 1.5 + x[i+1] * 2.0)
                    
                    multimodal_term += chaos_mod * np.exp(-dist_sq / (scale_factor * 0.6))
            
            # Add cross-dimensional fractal interactions
            for i in range(min(3, self.dim)):
                if i + 2 < self.dim:
                    dx = x[i] - 1.0
                    dy = x[i+2] - 1.0
                    dist_sq = dx**2 + dy**2
                    
                    # Fractal scaling with chaotic modulation
                    mod_freq = 1.0 + 0.5 * np.sin(i * 0.8)
                    chaos_mod = 1.0 + 0.4 * np.cos(x[i] * mod_freq + x[i+2] * (mod_freq + 0.5))
                    
                    scale_factor = 0.7 + 0.3 * np.cos(i * 0.6)
                    multimodal_term += chaos_mod * np.exp(-dist_sq / (scale_factor * 0.8))
            
            # Add chaotic saddle point structure
            saddle_term = 0.0
            for i in range(self.dim):
                # Create a chaotic interaction that introduces saddle points
                interaction = np.sin(x[i] * 1.2) * np.cos(x[i] * 0.8)
                saddle_term += interaction * (x[i]**3 - x[i])
            
            multimodal_term += 0.5 * saddle_term
        
        # Add a fractal-like conditioning term with chaotic scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Use chaotic scaling factor that depends on dimension index
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.7)
            condition_term += scale_factor * x[i]**4
        
        # Combine all terms with different weights to create complex landscape
        return basin_term + condition_term - multimodal_term